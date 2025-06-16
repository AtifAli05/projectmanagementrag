from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain_core.prompts import PromptTemplate

def build_rag_chain(vectorstore, llm):
    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True,
        output_key='answer'
    )
    
    # Custom prompt template for project management queries
    template = """You are an expert project management assistant. Use the following context to answer the question.
    
    Context:
    {context}
    
    Question: {question}
    
    Answer in this exact format:
    ### [Person's Name]
    **Projects:**
    - [Project Name 1] ([Type], [Status], [Dates])
    - [Project Name 2] ([Type], [Status], [Dates])
    **Departments:** [Department1, Department2]
    **Details:** [Additional relevant information]
    
    If you don't know the answer, say "I couldn't find information about [question] in the project data"."""
    
    QA_PROMPT = PromptTemplate(
        template=template,
        input_variables=["context", "question"]
    )
    
    retriever = vectorstore.as_retriever(
        search_kwargs={"k": 5}
    )
    
    return ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        memory=memory,
        combine_docs_chain_kwargs={"prompt": QA_PROMPT},
        return_source_documents=True,
        verbose=True
    )