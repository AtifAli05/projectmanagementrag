import os

folders = [
    "app/chains",
    "app/loaders",
    "app/retrievers",
    "app/embeddings",
    "app/prompts",
    "app/utils",
    "data/sample_docs",
    "ui",
    "tests"
]

files = {
    "app/config.py": "",
    "app/main.py": "",
    "requirements.txt": "",
    ".env": "# Put your API keys here\n",
    "README.md": "# RAG Chatbot Project\n",
    "tests/test_retriever.py": ""
}

for folder in folders:
    os.makedirs(folder, exist_ok=True)

for file_path, content in files.items():
    with open(file_path, "w") as f:
        f.write(content)

print("✅ Project structure created.")
