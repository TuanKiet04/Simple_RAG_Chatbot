from RAG.pipeline.offline_rag import offline_rag

if __name__ == "__main__":
    file_path = "sample.pdf"  # Đường dẫn file PDF thử nghiệm
    query = "What is attention mechanism?"
    response = offline_rag(file_path, query)
    print(response)