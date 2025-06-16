from langchain_huggingface import HuggingFaceEmbeddings

def getEmbeddings():
    return HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
