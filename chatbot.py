from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.vectorstores.utils import DistanceStrategy
from langchain_core.prompts import ChatPromptTemplate
from tqdm import tqdm
from dotenv import load_dotenv
import os

load_dotenv()

loader = DirectoryLoader (
    path = './docs',
    glob = '**/*.pdf',
    loader_cls = PyPDFLoader,
    show_progress = True,
    use_multithreading = True
)

docs = loader.load()

OPTIMIZED_SEPARATORS = [
    "\n\n",    
    "\n",   
    ". ",   
    "! ", 
    "? ",
    " ",  
    ""     
]

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,        
    chunk_overlap = 150,  
    add_start_index = True,
    strip_whitespace = True,
    separators = OPTIMIZED_SEPARATORS,
    is_separator_regex = False 
)

splits = text_splitter.split_documents(docs)
from pprint import pprint

from langchain_huggingface import HuggingFaceEndpointEmbeddings, ChatHuggingFace
from langchain_community.embeddings import HuggingFaceInferenceAPIEmbeddings

embeddings = HuggingFaceInferenceAPIEmbeddings(
    api_key=os.getenv('HF_API_key'), 
    model_name="sentence-transformers/all-MiniLM-L6-v2" 
)


vectorstore = FAISS.from_documents(
    documents = splits,
    embedding = embeddings,
    distance_strategy = DistanceStrategy.COSINE
)

retriever = vectorstore.as_retriever(
    search_type = 'similarity_score_threshold',
    search_kwargs={'k': 5, 'score_threshold': 0.2}
)

template = (
    '''
    You're a strict, citation-focused assistant for a private knowledge base. \n
    RULES:
    1. Use only the provided context to answer.\n
    2. If the answer is not clearly, just response you don't know.
    3. Do not use outside knowledge, guessing.
    'Context'\n{context}\n\n
    'Question' : {question}
    '''
)

prompt = ChatPromptTemplate.from_template(template)

llm = ChatHuggingFace(
    model = 'Qwen/Qwen3.5-0.8B',
    huggingfacehub_api_token=os.getenv('HF_API_key'),
    temperature = 0.1,
    top_k = 0.8
)

from langchain_core.output_parsers import StrOutPutParser
from langchain_core.runnables import RunnablePassthrough

rag_chain = (
    {'context': retriever, 'question': RunnablePassthrough}
    | prompt
    | llm
    | StrOutPutParser()
)

question = input('Ask something')

answer = rag_chain.invoke(question)

print(answer)