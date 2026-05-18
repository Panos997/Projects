## 🧠 Overview

**AI Semantic Keyword Retrieval System** is a mini experimental semantic search project developed during my work at **Kathimerini**.

The project started as a small internal R&D experiment using a limited base of clustered keywords, where each cluster represented a thematic category.

The main objective was to explore whether semantic search could retrieve relevant keywords based on meaning instead of relying only on exact word matching.

Although the project was built as a lightweight prototype, its long-term purpose was to explore an architecture that could later scale to significantly larger keyword datasets and more advanced retrieval workflows.

During development and testing, two different semantic retrieval approaches were evaluated:

1. **Pure Embeddings + Cosine Similarity**  
   A direct semantic comparison between the input text embedding and all keyword embeddings.

2. **FAISS HNSW Graph Search**  
   An approximate nearest-neighbor vector search using a graph-based retrieval structure for faster and more scalable semantic search.

Both approaches produced meaningful semantic results. However, as the keyword dataset increased, the FAISS HNSW approach demonstrated better performance due to its speed, scalability, and more efficient vector retrieval.

In summary:

- For smaller datasets, both approaches performed similarly.
- For larger keyword collections, the FAISS-based approach proved faster and more scalable.

---

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
