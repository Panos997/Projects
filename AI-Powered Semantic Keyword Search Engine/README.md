# Overview

**AI Semantic Keyword Retrieval System** is an experimental semantic search project developed during my work at **Kathimerini**.

The project was created as a small internal R&D prototype to explore how semantic AI retrieval systems can identify relevant keywords and concepts based on meaning instead of relying only on exact keyword matching.

Instead of searching using exact words, the system searches using semantic meaning.

The project combines:

- OpenAI Embeddings
- Semantic Vector Search
- FAISS HNSW Retrieval
- Approximate Nearest Neighbor Search

to build a lightweight semantic retrieval engine.

Although the system started as a mini prototype, its architecture was designed with scalability in mind, allowing future expansion to significantly larger keyword datasets and more advanced retrieval workflows.

---

# Project Goal

The main objective of the project was to test whether semantic search could retrieve relevant keywords from articles, phrases, or documents using semantic similarity instead of traditional text matching.

During development, two retrieval approaches were evaluated:

1. **Pure Embeddings + Cosine Similarity**  
   Direct semantic comparison between the query vector and all keyword embeddings.

2. **FAISS HNSW Graph Search**  
   Approximate nearest-neighbor vector retrieval using graph-based indexing.

Both methods produced meaningful semantic results. However, as the keyword dataset increased, the FAISS HNSW approach proved significantly faster and more scalable.

In summary:

- Small datasets → both methods performed similarly
- Large datasets → FAISS HNSW performed better due to scalability and retrieval speed

---

# How the System Works

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

---

# How It Works Step-by-Step

### 1. User Input

The user can provide:

- a short phrase
- a full article
- or a `.txt` file

Example:

```text
Artificial intelligence is transforming healthcare systems
```

---

### 2. Optional GPT Summarization

Before semantic retrieval begins, the system can optionally summarize the text using:

- GPT-4o
- GPT-4o-mini

This helps reduce noise and focus on the most important concepts before embedding generation.

---

### 3. Embedding Generation

The processed text is converted into embeddings using OpenAI embedding models.

Embeddings are numerical vector representations of semantic meaning.

Texts with similar meaning produce similar vectors.

---

### 4. FAISS HNSW Retrieval

All keywords from the dataset are converted into embeddings and stored inside a FAISS HNSW vector index.

The system compares the query embedding against the stored keyword embeddings and retrieves the closest semantic matches.

Unlike traditional keyword search, the system retrieves concepts based on semantic similarity instead of exact word matching.

---

### 5. Final Results

The system returns the most semantically relevant keywords ranked by similarity score.

Example output:

```text
artificial intelligence
machine learning
healthcare
medical innovation
```

---

# 📂 What the System Requires

Before using the application, the following are required:

## 1. OpenAI API Key

Used for:

- embedding generation
- GPT summarization

---

## 2. Gemini API Key

Used for optional summarization workflows.

---

## 3. Keyword Dataset (CSV)

The application requires a CSV file containing keywords.

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

These keywords form the semantic retrieval space of the system.

---

# Project Structure

```text
AI Semantic Keyword Retrieval System/
│
├── app.py
├── requirements.txt
├── README.md
└── experimentation.ipynb
```

---

# File Explanation

## `app.py`

Main semantic search application.

Responsible for:

- loading the dataset
- generating embeddings
- building the FAISS index
- semantic retrieval
- result ranking

---

## `requirements.txt`

Contains all required Python libraries.

Install them using:

```bash
pip install -r requirements.txt
```

---

# Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

---

# Startup Flow

When the application starts, it asks for:

1. OpenAI API Key
2. Gemini API Key
3. CSV keyword dataset path

The system then:

- generates embeddings
- builds the FAISS HNSW index
- initializes semantic retrieval
- starts the search workflow

---

# What This Project Demonstrates

This project demonstrates:

- semantic search
- vector embeddings
- vector databases
- approximate nearest-neighbor retrieval
- scalable semantic keyword matching
- AI-powered information retrieval pipelines

The architecture is conceptually similar to systems used in:

- RAG pipelines
- AI assistants
- recommendation systems
- enterprise semantic search
- intelligent document retrieval systems
- vector database workflows

---

# Conclusion

This project demonstrates how modern AI retrieval systems can move beyond traditional keyword matching and perform semantic understanding through embeddings and vector search.

Although developed as a lightweight prototype, the system was designed to explore scalable semantic retrieval architectures that could later support larger datasets and more advanced AI search workflows.
