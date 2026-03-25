# Simple RAG Chatbot

This repository contains a small pipeline of a **Retrieval-Augmented Generation (RAG)** chatbot designed to interact with private PDF documents.

---

## 📂 Project Structure
The repository is organized into the following components:

* **`chatbot.py`**: The core RAG implementation (Load, Split, Embed, and Retrieve).
* **`frontend/`**: The UI layer (not finished)
* **`backend/`**: The API service layer using FASTAPI (not finished)
* **`docs/`**: Directory for storing local PDF documents used as the knowledge base (tested on 1 PDF).

---

## 🛠 Technical Stack
* **Orchestration**: [LangChain](https://github.com/langchain-ai/langchain) for managing the RAG pipeline.
* **Document Processing**: `PyPDFLoader` for extracting text from PDFs.
* **Text Splitting**: `RecursiveCharacterTextSplitter` with optimized separators for maintaining semantic context.
* **Vector Store**: [FAISS]for efficient similarity search and local vector storage.
* **Models**: HuggingFace Inference API.

---

> **Note**: This project is currently a work in progress. Some modules in the `frontend/` and `backend/` directories are undergoing heavy refactoring to integrate with the core RAG logic.
