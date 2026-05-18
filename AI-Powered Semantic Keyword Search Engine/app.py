# -*- coding: utf-8 -*-
"""
semantic_search_oneflow.py
--------------------------------
Ενιαία εφαρμογή semantic search πάνω σε μικρό keyword graph με FAISS + OpenAI.

Flow εκκίνησης:
1) Ζητά 2 API keys (OPENAI_API_KEY + GEMINI_API_KEY).
2) Ζητά διαδρομή CSV (στήλη 'keyword' ή 1η στήλη).
3) Χτίζει/ξαναχτίζει index (FAISS HNSW).
4) Loop: ο χρήστης δίνει ΦΡΑΣΗ ή ΟΛΟΚΛΗΡΟ ΑΡΘΡΟ ή PATH σε .txt,
   και επιλέγει αν θέλει GPT-4o(-mini) περίληψη πριν το semantic search.

Απαιτήσεις:
pip install faiss-cpu numpy pandas python-dotenv openai>=1.0.0 rapidfuzz
"""

import os, re, uuid, getpass
from pathlib import Path
import numpy as np
import pandas as pd
from dotenv import load_dotenv
from openai import OpenAI
import faiss
from rapidfuzz import fuzz

# ================== ΡΥΘΜΙΣΕΙΣ ==================
load_dotenv()

EMBED_MODEL = os.getenv("EMBED_MODEL", "text-embedding-3-large")
DIM = 3072
NORMALIZE = True
BATCH = 128

INDEX_DIR = Path("vector_index")
INDEX_PATH = INDEX_DIR / "hnsw.index"
META_PATH  = INDEX_DIR / "meta.parquet"

# ---- ΔΕΥΤΕΡΟ API KEY: GEMINI ----
GEMINI_API_KEY_NAME = "GEMINI_API_KEY"  # env var name για Gemini


# ================== ΒΟΗΘΗΤΙΚΑ ==================
def clean_text(t: str) -> str:
    return re.sub(r"\s+", " ", str(t)).strip()

def normalize_rows(x: np.ndarray) -> np.ndarray:
    n = np.linalg.norm(x, axis=1, keepdims=True) + 1e-12
    return x / n

def ask_yesno(msg: str, default_yes=True) -> bool:
    suffix = "[Y/n]" if default_yes else "[y/N]"
    ans = input(f"{msg} {suffix} ").strip().lower()
    if not ans:
        return default_yes
    return ans in ("y", "yes", "nai", "ναι")

def summarize_with_gpt(text: str, model: str = "gpt-4o-mini", api_key: str = "") -> str:
    """
    Σύντομη περίληψη (<=80 λέξεις) για semantic search.
    Βάλε model="gpt-4o" αν θέλεις full 4o.
    """
    try:
        client = OpenAI(api_key=api_key)
        resp = client.chat.completions.create(
            model=model,
            messages=[{
                "role": "user",
                "content": (
                    "Δώσε πολύ σύντομη περίληψη (<=80 λέξεις) "
                    "με τις βασικές έννοιες για semantic search:\n\n" + text
                )
            }],
            temperature=0.0
        )
        summ = (resp.choices[0].message.content or "").strip()
        return summ if summ else text
    except Exception as e:
        print(f"!! Απέτυχε το summarization ({e}). Συνεχίζω με αρχικό κείμενο.")
        return text

def embed_texts(client, texts):
    embs = []
    for i in range(0, len(texts), BATCH):
        chunk = texts[i:i+BATCH]
        resp = client.embeddings.create(model=EMBED_MODEL, input=chunk)
        embs.extend([e.embedding for e in resp.data])
    X = np.array(embs, dtype="float32")
    return normalize_rows(X) if NORMALIZE else X

def embed_one(client, text: str) -> np.ndarray:
    resp = client.embeddings.create(model=EMBED_MODEL, input=[text])
    v = np.array([resp.data[0].embedding], dtype="float32")
    return normalize_rows(v) if NORMALIZE else v

def read_keywords_csv(path: Path, column: str | None = None, columns: str | None = None) -> list[str]:
    """
    Υποστηρίζει:
    - 1 στήλη: --column <name> (ή αν λείπει, παίρνει 'keyword' ή την 1η στήλη)
    - Πολλές στήλες: columns="col1,col2,..." (ενώνει όλες τις τιμές)
    Κάθε κελί => ένα keyword (trim), αφαιρεί διπλότυπα/κενά, κρατά σειρά.
    """
    df = pd.read_csv(path)

    def clean_series(s: pd.Series) -> list[str]:
        seen, out = set(), []
        for x in s.astype(str):
            t = clean_text(x)
            if t and t not in seen:
                seen.add(t); out.append(t)
        return out

    if columns:
        cols = [c.strip() for c in columns.split(",") if c.strip()]
        missing = [c for c in cols if c not in df.columns]
        if missing:
            raise ValueError(f"Δεν βρέθηκαν στήλες: {missing}")
        combined = []
        for c in cols:
            combined.extend(clean_series(df[c]))
        # μοναδικά με διατήρηση σειράς
        seen, out = set(), []
        for t in combined:
            if t not in seen:
                seen.add(t); out.append(t)
        return out

    if column:
        if column not in df.columns:
            raise ValueError(f"Δεν υπάρχει στήλη '{column}' στο CSV.")
        return clean_series(df[column])

    if "keyword" in df.columns:
        return clean_series(df["keyword"])
    return clean_series(df.iloc[:, 0])

def read_maybe_file(user_input: str) -> str:
    """
    Αν ο χρήστης έδωσε path σε .txt που υπάρχει -> διάβασε αρχείο.
    Αλλιώς, επέστρεψε την ίδια τη φράση/άρθρο που επικόλλησε.
    """
    p = Path(user_input.strip().strip('"').strip("'"))
    if p.suffix.lower() == ".txt" and p.exists():
        return p.read_text(encoding="utf-8")
    return user_input


# ================== INDEX OPS ==================
def build_index_from_keywords(keywords: list[str], openai_key: str):
    if not keywords:
        raise ValueError("Άδεια λίστα keywords.")
    INDEX_DIR.mkdir(exist_ok=True, parents=True)

    client = OpenAI(api_key=openai_key)
    X = embed_texts(client, keywords)

    idx = faiss.IndexHNSWFlat(DIM, 64, faiss.METRIC_INNER_PRODUCT)
    idx.hnsw.efConstruction = 200
    idx.hnsw.efSearch = 64
    idx.add(X)

    meta = pd.DataFrame({
        "doc_id": [str(uuid.uuid4()) for _ in keywords],
        "keyword": keywords
    })
    faiss.write_index(idx, str(INDEX_PATH))
    meta.to_parquet(META_PATH, index=False)
    print(f"OK: Φτιάχτηκε index με {idx.ntotal} keywords.")

def load_index_and_meta():
    if not (INDEX_PATH.exists() and META_PATH.exists()):
        raise RuntimeError("Δεν βρέθηκε index. Χτίσε τον πρώτα.")
    idx = faiss.read_index(str(INDEX_PATH))
    meta = pd.read_parquet(META_PATH)
    return idx, meta


# ================== ΕΚΚΙΝΗΣΗ (Credentials + CSV) ==================
def interactive_collect_credentials_and_csv():
    print("=== Ρυθμίσεις Εκκίνησης ===")
    openai_key = os.getenv("OPENAI_API_KEY", "").strip()
    gemini_key  = os.getenv(GEMINI_API_KEY_NAME, "").strip()

    if not openai_key:
        print("Δώσε OPENAI_API_KEY (δεν θα φαίνεται):")
        openai_key = getpass.getpass("OPENAI_API_KEY: ").strip()
        if not openai_key:
            raise RuntimeError("Χρειάζεται OPENAI_API_KEY.")

    if not gemini_key:
        print(f"Δώσε {GEMINI_API_KEY_NAME} (κλειδί Gemini, δεν θα φαίνεται):")
        gemini_key = getpass.getpass(f"{GEMINI_API_KEY_NAME}: ").strip()
        if not gemini_key:
            raise RuntimeError(f"Χρειάζεται {GEMINI_API_KEY_NAME}.")

    # Βάλε τα και στο περιβάλλον για runtime
    os.environ["OPENAI_API_KEY"] = openai_key
    os.environ[GEMINI_API_KEY_NAME] = gemini_key

    # CSV path
    while True:
        csv_path_str = input("Δώσε διαδρομή CSV με keywords (π.χ. data/keywords.csv): ").strip().strip('"').strip("'")
        if not csv_path_str:
            print("Παρακαλώ γράψε διαδρομή.")
            continue
        csv_path = Path(csv_path_str)
        if not csv_path.exists():
            print(f"Δεν βρέθηκε αρχείο: {csv_path}")
            continue
        try:
            # Αν θέλεις συγκεκριμένες στήλες, πες μου να το ρωτάει εδώ (column/columns).
            kws = read_keywords_csv(csv_path)
            if not kws:
                print("Το CSV φαίνεται άδειο. Δώσε άλλο αρχείο.")
                continue
            return openai_key, gemini_key, csv_path, kws
        except Exception as e:
            print(f"Σφάλμα ανάγνωσης CSV: {e}. Δώσε άλλο αρχείο.")


# ================== APP FLOW ==================
def main():
    # 1) Ζήτα 2 keys + CSV στην αρχή
    openai_key, gemini_key, csv_path, keywords = interactive_collect_credentials_and_csv()

    print("\nTip: Στο επόμενο βήμα μπορείς να επικολλήσεις ολόκληρο άρθρο ή απλώς να δώσεις μια φράση.")
    print("Αν δώσεις path σε .txt, θα διαβάσει το αρχείο.\n")

    # 2) Χτίσε index (αν υπάρχει ήδη, ρώτα)
    if INDEX_PATH.exists() or META_PATH.exists():
        if ask_yesno("Υπάρχει ήδη index. Θες να τον ξαναχτίσω από το CSV;", default_yes=False):
            build_index_from_keywords(keywords, openai_key)
    else:
        build_index_from_keywords(keywords, openai_key)

    # 3) Ενιαίο flow: δώσε ΦΡΑΣΗ ή ΑΡΘΡΟ ή PATH σε .txt
    while True:
        print("\n=== Semantic Search ===")
        user_in = input("Γράψε φράση/επικόλλησε άρθρο ή δώσε path σε .txt (Enter για έξοδο): ").strip()
        if not user_in:
            print("Έξοδος. 👋")
            break

        try:
            raw_text = read_maybe_file(user_in)

            # Ρώτα αν θέλει GPT-4o περίληψη πριν το embedding
            if ask_yesno("Θες GPT-4o περίληψη πριν το semantic search;", default_yes=True):
                use_full = ask_yesno("Να χρησιμοποιήσω το gpt-4o (όχι mini);", default_yes=False)
                model = "gpt-4o" if use_full else "gpt-4o-mini"
                text_for_search = summarize_with_gpt(raw_text, model=model, api_key=openai_key)
                print("\n--- Περίληψη που θα χρησιμοποιηθεί για embedding ---")
                print(text_for_search[:800], "...\n" if len(text_for_search)>800 else "\n")
            else:
                text_for_search = raw_text

            # Semantic search
            client = OpenAI(api_key=openai_key)
            idx, meta = load_index_and_meta()
            qv = embed_one(client, clean_text(text_for_search))
            k = 10
            topn = min(max(k*5, k), len(meta))
            D, I = idx.search(qv, topn)

            cand = meta.iloc[I[0]].copy()
            cand["score_vec"] = D[0]
            cand["keyword_boost"] = cand["keyword"].fillna("").apply(
                lambda t: fuzz.token_set_ratio(text_for_search, str(t))/100.0
            )
            cand["final_score"] = 0.9*cand["score_vec"] + 0.1*cand["keyword_boost"]

            res = cand.sort_values("final_score", ascending=False).head(k)[["keyword","final_score"]]
            print("\nΑποτελέσματα:")
            print(res.to_string(index=False))

            # Προαιρετική αποθήκευση αποτελεσμάτων
            if ask_yesno("Να αποθηκεύσω τα αποτελέσματα σε CSV;", default_yes=False):
                out_path = Path("semantic_results.csv")
                res.to_csv(out_path, index=False, encoding="utf-8")
                print(f"OK: Αποθηκεύτηκαν στο {out_path.resolve()}")

        except Exception as e:
            print(f"Σφάλμα: {e}")


if __name__ == "__main__":
    main()
