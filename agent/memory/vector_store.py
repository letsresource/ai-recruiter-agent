from langchain_openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS

def create_vector_store(texts):
    embeddings = OpenAIEmbeddings()
    return FAISS.from_texts(texts, embeddings)
