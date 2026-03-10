# Wisdom AI 🧠

**Wisdom AI** is an intelligent organizational teammate designed to bridge the gap between fragmented team communication and actionable knowledge. By processing data across Discord, Zoom transcripts, and document uploads, Wisdom AI builds a unified, persistent "Team Brain." It ensures that key discussions, decisions, and tasks are never lost in the noise.

---

## 🚀 Key Features

* **Unified Context Ingestion:** Seamlessly aggregates data from disparate sources: Discord conversations, Zoom meeting transcripts, and manual file uploads (PDF, DOCX, TXT).
* **Dynamic Knowledge Base:** Automatically structures unstructured conversational data into a searchable, high-fidelity knowledge repository.
* **Intelligent Chat Interface:** A **Streamlit-powered** dashboard that allows team members to query the entire organizational history using natural language.
* **Adaptive Personalization:** Uses **mem0** to remember user-specific preferences and past interactions, ensuring the AI's utility grows the more the team uses it.
* **High-Precision Retrieval:** Implements a **Two-Stage Retrieval** pipeline using a **Reranker** to ensure that the most contextually relevant information is surfaced, not just the most "similar" text.

---

## 🛠️ Tech Stack

| Layer | Technology |
| :--- | :--- |
| **Backend Framework** | FastAPI (Python) |
| **Frontend / UI** | Streamlit |
| **Memory Management** | mem0 (Long-term user & team memory) |
| **Vector Database** | Qdrant (High-performance vector search) |
| **Orchestration** | LangGraph (Stateful workflow management) |
| **Optimization** | Coherent reranker |

---

## 🏗️ Technical Highlights

### Memory-Augmented RAG with mem0
Wisdom AI utilizes **mem0** to provide a persistent memory layer. Unlike standard RAG systems that treat every query as a fresh start, Wisdom AI:
* Tracks evolving project contexts over time, leading to more relevant responses in long-term team projects.

### Optimized Retrieval Pipeline (Qdrant + Reranker)
1.  **Stage 1 (Retrieval):** Qdrant performs a fast semantic search across millions of vector embeddings.
2.  **Stage 2 (Reranking):** A **Cross-Encoder Reranker** scores the top results against the query, filtering out noise and ensuring the LLM only receives the highest-quality context. This significantly reduces hallucinations and increases answer accuracy.
