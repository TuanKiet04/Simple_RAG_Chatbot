from langchain.llms.huggingface_pipeline import HuggingFacePipeline
from transformers import pipeline

def get_LLM(model_name):
    model_pipeline = pipeline("text-generation", model=model_name)
    return HuggingFacePipeline(pipeline=model_pipeline)
