## ⚙️ How the System Works

The application performs semantic keyword retrieval through the following pipeline:

```text
User Input
    ↓
Optional GPT Summarization
    ↓
Text Embedding Generation
    ↓
FAISS Vector Search
    ↓
Top Semantic Keyword Matches
```

### How it works

The user can enter:

- a short phrase
- a full article
- or a `.txt` file

Before the search begins, the system can optionally summarize the text using GPT-4o or GPT-4o-mini in order to focus on the most important concepts.

The processed text is then converted into embeddings (semantic vectors) using OpenAI embedding models.

At the same time, all keywords from the dataset are also converted into embeddings and stored inside a FAISS HNSW vector index.

The system compares the input vector with the stored keyword vectors and retrieves the most semantically relevant matches.

Unlike traditional keyword search, the system searches based on semantic meaning rather than exact word matching.

---

## 📂 What the System Requires

Before using the application, the following are required:

### 1. OpenAI API Key

Used for:

- text embeddings
- GPT summarization

---

### 2. Gemini API Key

Used for optional summarization workflows inside the application.

---

### 3. Keyword Dataset (CSV)

The system requires a CSV file containing keywords.

The CSV must contain a column named:

```text
keyword
```

Example:

```csv
keyword
artificial intelligence
machine learning
healthcare
economy
football
music
```

These keywords form the semantic search space used by the retrieval engine.

---

## 🚀 Running the Application

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

When the application starts, it will ask for:

1. OpenAI API Key
2. Gemini API Key
3. CSV keyword dataset path

After initialization, the system builds the FAISS vector index and starts the semantic search workflow.
