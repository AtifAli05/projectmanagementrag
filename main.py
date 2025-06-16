# from embeddings.huggingFaceEmbddings import getEmbeddings
from app.embeddings.huggingFaceEmbddings import getEmbeddings
from app.retrievers.chromaRetriver import getVectorStore
from app.prompts.basePrompts import getRagPrompts
from app.chains.ragChain import build_rag_chain
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from app.loaders.csvLoader import loadCsvDocs
import os

def main():
    load_dotenv()
    docs = loadCsvDocs("data/sample_docs/")
    embeddings = getEmbeddings()
    vectorstore = getVectorStore(docs, embeddings)

    # Gemini model
    llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",  # Or "gemini-pro" if your API key supports it
    temperature=0,
    google_api_key=os.getenv("GOOGLE_API_KEY"))

    rag_chain = build_rag_chain(vectorstore, llm)

    while True:
        try:
            query = input("\nQuestion: ")
            if query.lower() in ["exit", "quit"]:
                break
                
            result = rag_chain.invoke({"question": query})
            
            print("\n=== Answer ===")
            print(result["answer"])
            
            # Show sources for verification
            print("\n=== Sources ===")
            for i, doc in enumerate(result["source_documents"][:3], 1):
                print(f"\nSource {i}:")
                print(f"File: {doc.metadata.get('source_file', 'Unknown')}")
                print(f"Content: {doc.page_content[:200]}...")
                
        except Exception as e:
            print(f"\nError: {str(e)}")
            
if __name__ == "__main__":
    main()
