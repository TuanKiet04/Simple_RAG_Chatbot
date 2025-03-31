from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from .base_vectordb import BaseVectorDB

class FAISSDB(BaseVectorDB):
    def __init__(self, documents, embedding_model):
        super().__init__(documents, embedding_model)
        self.embeddings = HuggingFaceEmbeddings(model_name=embedding_model)
        self.db = FAISS.from_documents(documents, self.embeddings)
    def retrieval(self, query, k=5):
        return self.db.similarity_search(query, k=k)
