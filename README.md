# Simple RAG Chatbot

This repository contains the development of a **Retrieval-Augmented Generation (RAG)** chatbot designed to interact with private PDF documents. It features a modular structure including a dedicated Frontend and Backend.

---

## 📂 Project Structure
The repository is organized into the following components:

* **`chatbot.py`**: The core RAG implementation (Load, Split, Embed, and Retrieve).
* **`frontend/`**: The UI layer (built with React/Vite using **WebSocket** for real-time communication).
* **`backend/`**: The API service layer (FastAPI) to handle document processing and model orchestration.
* **`docs/`**: Directory for storing local PDF documents used as the knowledge base.

---

## 🛠 Technical Stack
* **Orchestration**: [LangChain](https://github.com/langchain-ai/langchain) for managing the RAG pipeline.
* **Document Processing**: `PyPDFLoader` for extracting text from PDFs.
* **Text Splitting**: `RecursiveCharacterTextSplitter` with optimized separators for maintaining semantic context.
* **Vector Store**: [FAISS](https://github.com/facebookresearch/faiss) for efficient similarity search and local vector storage.
* **Models**: Integrated with **Ollama** (Local LLMs) and **HuggingFace Inference API**.
* **Communication**: **WebSocket (WS)** implementation for low-latency chat interactions between FE and BE.

---

> **Note**: This project is currently a work in progress. Some modules in the `frontend/` and `backend/` directories are undergoing heavy refactoring to integrate with the core RAG logic.
