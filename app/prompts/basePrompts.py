from langchain.prompts import PromptTemplate

def getRagPrompts():
    template = """You are an expert project management assistant analyzing CSV data. 
    Always provide COMPLETE information from the context. For people queries, include:
    - All projects they managed
    - Project types
    - Departments
    - Statuses
    - Time periods
    
    Context: {context}
    
    Question: {question}
    
    Provide a detailed response in this format:
    ### [Name]
    **Role:** [Role if available]
    **Projects Managed:**
    - [Project 1] ([Type], [Status], [Dates])
    - [Project 2] ([Type], [Status], [Dates])
    **Departments:** [List of departments]
    **Additional Info:** [Any other relevant details]
    
    Answer:"""
    
    return PromptTemplate(
        template=template,
        input_variables=["context", "question"]
    )