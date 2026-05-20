# AI Semantic Keyword Retrieval System

## Overview

AI Semantic Keyword Retrieval System is an experimental semantic search application designed to retrieve relevant keywords based on semantic meaning instead of exact keyword matching.

The project was developed as an internal R&D prototype to explore how AI embeddings and vector search can improve keyword retrieval workflows for articles, documents, and text content.

Instead of searching using exact words, the system converts text into embeddings and retrieves the most semantically similar keywords from a vector index.

The project combines:

- OpenAI Embeddings
- FAISS Vector Search
- HNSW Approximate Nearest Neighbor Retrieval
- GPT-based text summarization

to build a lightweight semantic retrieval engine.

---

# What the Application Does

The application receives:

- a phrase
- a full article
- or a `.txt` file

and returns the most semantically relevant keywords from a keyword dataset.

Example:

### Input

```text
Artificial intelligence is transforming healthcare systems through automation.
```

### Output

```text
artificial intelligence
machine learning
healthcare
medical innovation
automation
```

The system does not rely only on exact words.

Instead, it retrieves keywords based on semantic similarity and contextual meaning.

---

# How It Works

The workflow of the application is:

```text
User Input
      ↓
Optional GPT Summarization
      ↓
Embedding Generation
      ↓
FAISS Vector Search
      ↓
Semantic Keyword Retrieval
      ↓
Ranked Results
```

---

# How the Retrieval Process Works

## 1. User Input

The user can provide:

- a short phrase
- a full article
- or a path to a `.txt` file

The application automatically detects whether the input is plain text or a file path.

---

## 2. Optional GPT Summarization

Before semantic retrieval begins, the system can optionally summarize the text using:

- GPT-4o
- GPT-4o-mini

This helps reduce noise and focus on the most important concepts before embedding generation.

---

## 3. Embedding Generation

The text is converted into embeddings using OpenAI embedding models.

Embeddings are numerical vector representations of semantic meaning.

Texts with similar meaning produce similar embedding vectors.

The project uses:

```text
text-embedding-3-large
```

as the embedding model. :contentReference[oaicite:0]{index=0}

---

## 4. FAISS HNSW Retrieval

All keywords from the dataset are embedded and stored inside a FAISS HNSW vector index.

The query embedding is compared against the stored keyword embeddings to retrieve the closest semantic matches.

The retrieval uses:

- FAISS
- HNSW graph indexing
- Approximate Nearest Neighbor Search

to improve scalability and retrieval speed.

---

## 5. Hybrid Ranking

After vector retrieval, the system applies additional keyword similarity scoring using:

```python
rapidfuzz.fuzz.token_set_ratio()
```

This creates a hybrid scoring mechanism that combines:

- semantic similarity
- keyword overlap similarity

Final ranking formula:

```text
0.9 * vector similarity
+ 0.1 * keyword similarity
```

---

## 6. Final Results

The application returns the top semantic keyword matches ranked by relevance score.

Example:

```text
machine learning
healthcare
medical innovation
predictive analytics
artificial intelligence
```

---

# Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| OpenAI API | Embeddings + GPT summarization |
| FAISS | Vector similarity search |
| HNSW | Approximate nearest-neighbor retrieval |
| NumPy | Vector operations |
| Pandas | CSV handling and metadata |
| RapidFuzz | Keyword similarity scoring |
| Python Dotenv | Environment variable management |
| Jupyter Notebook | Experimentation and testing |

The project dependencies are listed in `requirements.txt`: :contentReference[oaicite:1]{index=1}

```text
faiss-cpu
numpy
pandas
python-dotenv
openai>=1.0.0
rapidfuzz
```

---

# Project Structure

```text
AI Semantic Keyword Retrieval System/
│
├── app.py
├── experimentation.ipynb
├── requirements.txt
└── README.md
```

---

# File Explanation

## `app.py`

Main semantic retrieval application. :contentReference[oaicite:2]{index=2}

Responsible for:

- loading keyword datasets
- generating embeddings
- building the FAISS index
- semantic retrieval
- hybrid ranking
- CSV result export
- interactive search flow

The file contains the complete retrieval pipeline and CLI workflow.

---

## `experimentation.ipynb`

Notebook used for experimentation and testing.

Used during development for:

- prompt testing
- embedding experimentation
- retrieval testing
- semantic similarity experiments
- FAISS evaluation

---

## `requirements.txt`

Contains all required dependencies for the project. :contentReference[oaicite:3]{index=3}

Install them using:

```bash
pip install -r requirements.txt
```

---

# How to Run the Project

## 1. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 2. Set API Keys

The project requires:

- OpenAI API Key
- Gemini API Key

Example:

### Linux / macOS

```bash
export OPENAI_API_KEY="your_openai_key"
export GEMINI_API_KEY="your_gemini_key"
```

### Windows PowerShell

```powershell
$env:OPENAI_API_KEY="your_openai_key"
$env:GEMINI_API_KEY="your_gemini_key"
```

---

## 3. Run the Application

```bash
python app.py
```

The application starts as an interactive terminal workflow.

---

# Startup Flow

When the application starts, it asks for:

1. OpenAI API Key
2. Gemini API Key
3. CSV dataset path

The system then:

- loads the keyword dataset
- generates embeddings
- builds the FAISS HNSW index
- initializes semantic retrieval

---

# Dataset Requirements

The application requires a CSV file containing keywords.

The CSV should contain either:

- a column named `keyword`
- or keywords in the first column

Example:

```csv
keyword
artificial intelligence
machine learning
healthcare
economy
sports
technology
```

These keywords become the searchable semantic retrieval space.

---

# Technical Details

# Architecture

The project follows this architecture:

```text
User Query
      ↓
Optional GPT Summarization
      ↓
OpenAI Embedding Generation
      ↓
FAISS HNSW Vector Search
      ↓
Hybrid Similarity Ranking
      ↓
Top Semantic Results
```

---

# Embedding Pipeline

The project uses:

```python
client.embeddings.create()
```

from the OpenAI SDK to generate vector embeddings. :contentReference[oaicite:4]{index=4}

The embedding model is:

```text
text-embedding-3-large
```

with vector dimension:

```text
3072
```

---

# Vector Indexing

The system builds a FAISS HNSW index using:

```python
faiss.IndexHNSWFlat()
```

Configured with:

- HNSW graph search
- Inner product similarity
- Embedding normalization
- Approximate nearest-neighbor retrieval

This improves retrieval performance for larger keyword datasets.

---

# Semantic Search Logic

The semantic search process:

1. Embed the query text
2. Search nearest vectors in FAISS
3. Retrieve top candidate keywords
4. Apply keyword similarity boost
5. Re-rank results
6. Return top matches

---

# Hybrid Scoring System

The project combines:

- vector similarity
- fuzzy keyword similarity

to improve ranking quality.

Keyword boosting uses:

```python
rapidfuzz.fuzz.token_set_ratio()
```

This helps improve retrieval for partially matching phrases.

---

# Summarization Workflow

Before embedding generation, the system can optionally summarize long text using:

- GPT-4o
- GPT-4o-mini

The summary is then embedded instead of the full article.

This helps reduce embedding noise and improve semantic retrieval quality.

---

# Result Export

The application can optionally save results as:

```text
semantic_results.csv
```

This allows retrieval outputs to be reused outside the application.

---

# Example Usage

## Example 1

### Input

```text
Machine learning is increasingly used in banking systems to detect fraud and improve risk analysis.
```

### Output

```text
machine learning
finance
fraud detection
risk analysis
artificial intelligence
```

---

## Example 2

### Input

```text
Climate change is affecting agriculture and global food production.
```

### Output

```text
climate change
agriculture
food production
environment
global warming
```

---

# What This Project Demonstrates

This project demonstrates:

- semantic search systems
- vector embeddings
- approximate nearest-neighbor retrieval
- FAISS vector indexing
- hybrid semantic ranking
- scalable retrieval architectures
- AI-powered keyword retrieval
- semantic understanding workflows

The architecture is conceptually related to systems used in:

- RAG pipelines
- AI search engines
- recommendation systems
- vector databases
- intelligent retrieval systems
- semantic document search

---

# Conclusion

AI Semantic Keyword Retrieval System demonstrates how modern AI retrieval pipelines can move beyond traditional keyword matching and perform semantic search using embeddings and vector similarity.

The project combines OpenAI embeddings, FAISS HNSW indexing, and hybrid ranking techniques to create a scalable semantic keyword retrieval workflow for articles and text content.
