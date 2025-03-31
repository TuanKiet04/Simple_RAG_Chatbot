class BaseVectorDB:
    def __init__(self, documents, embedding_model):
        self.documents = documents
        self.embedding_model = embedding_model
    def retrieval(self, query):
        raise NotImplementedError("Must implement retrieval method")