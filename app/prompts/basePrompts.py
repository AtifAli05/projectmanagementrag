from langchain_core.prompts import PromptTemplate

GENERIC_PROMPT = PromptTemplate(
    input_variables=["context", "question"],
    template="""
You are a smart assistant trained to analyze and summarize multi-domain data. Use the following context to answer the user's question precisely. Do not repeat the same facts.

If multiple rows or sources say the same thing, combine them once.

Context:
{context}

Question: {question}

Answer:
- **Topic:** [Auto-detected]
- **Key Details:**
  - [Summarized Facts]

If not found: "I couldn’t find specific information about '[question]' in the available data."
"""
)
