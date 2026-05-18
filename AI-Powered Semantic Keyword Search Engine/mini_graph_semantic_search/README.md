<p align="center">
  <h1 align="center">Mini Semantic Search Graph</h1>
  <p align="center"><b>Experimental Semantic Search App using OpenAI + FAISS HNSW</b></p>
</p>

---

## 🧠 Overview

**Mini Semantic Search Graph** is an **experimental project** built during internal R&D testing.  
We started with a **small base of clustered keywords**, each cluster representing a thematic category.  
Initially, we tested two approaches for semantic retrieval:

1. **Pure Embeddings + Cosine Similarity** — a direct method comparing the article vector with all keyword embeddings.  
2. **FAISS HNSW Graph** — an approximate nearest-neighbor search over all keyword vectors.

Both methods produced **strong and meaningful results** in terms of semantic relevance.  
However, as the number of keywords increased, the **FAISS graph performed better**,  
mainly due to its **speed and scalability**, allowing efficient searches even with thousands of entries.  

In summary: *for smaller datasets, both work equally well;  
for larger keyword bases, the FAISS-based approach is faster and more robust.*


## ⚙️ What It Does

The app lets you:
- 🔍 Enter a **phrase**, **full article**, or a **.txt file**
- ✨ Optionally summarize it with **GPT-4o** or **GPT-4o-mini** before searching
- 🧾 Retrieve the **most relevant keywords** from your dataset

Before searching, the app prompts you to **upload your mini keyword dataset** —  
a simple **CSV file** with **one column named `keyword`** containing all the terms or phrases  
that will form the semantic search space.


## 📁 Project Structure

| File / Folder | Description |
|----------------|-------------|
| `app.py` | Main interactive app |
| `requirements.txt` | Dependencies |
| `experiments/` | Colab tests and sample experiments *(no company data included)* |

---

## 🚀 Setup

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the app
python app.py
