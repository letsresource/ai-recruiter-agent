from langchain.document_loaders import PyPDFLoader

def load_resume(pdf_path):
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()
    text = " ".join([doc.page_content for doc in documents])
    return text
