from langchain_community.vectorstores import Chroma

def getVectorStore(docs, embeddings, persist_path="chroma_db"):
    return Chroma.from_documents(docs, embedding=embeddings, persist_directory=persist_path)
