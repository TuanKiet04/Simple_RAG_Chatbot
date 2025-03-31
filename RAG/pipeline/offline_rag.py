from ..vectordb.faiss_db import FAISSDB
from ..llm.llm_model import get_LLM
from ..loaders.text_splitter import split_text
from ..config import CONFIG
from ..loaders.pdf_loader import PDFLoader

def offline_rag(file_path, query):
    # Load & split text
    loader = PDFLoader()
    text = loader.load(file_path)
    chunks = split_text(text, CONFIG["chunk_size"], CONFIG["chunk_overlap"])
    
    # Tạo vectorDB
    vector_db = FAISSDB(chunks, CONFIG["embedding_model"])
    retriever = vector_db.retrieval(query)
    
    # Gọi LLM
    llm = get_LLM(CONFIG["llm_model"])
    response = llm.run(retriever)
    return response
