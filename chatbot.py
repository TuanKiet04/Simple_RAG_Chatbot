from langchain_community.document_loaders import DirectoryLoader

from langchain_community.document_loaders import PyPDFLoader

from tqdm import tqdm


loader = DirectoryLoader (
    path = './docs',
    glob = '**/*.pdf',
    loader_cls = PyPDFLoader,
    show_progress = True,
    use_multithreading = True
)

docs = loader.load()
print(len(docs))
print(docs)