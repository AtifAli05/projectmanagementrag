import pandas as pd
from langchain_core.documents import Document
from typing import List
import os

def loadCsvDocs(directory: str) -> List[Document]:
    """Robust CSV loader that handles all your files"""
    all_docs = []
    
    for filename in os.listdir(directory):
        if filename.endswith('.csv'):
            try:
                filepath = os.path.join(directory, filename)
                
                # Read CSV with pandas - handles BOM and different formats
                df = pd.read_csv(filepath, encoding='utf-8-sig')
                
                # Clean column names (remove BOM if present)
                df.columns = df.columns.str.replace('\ufeff', '')
                
                # Convert each row to a Document
                for _, row in df.iterrows():
                    # Create page content
                    content = "\n".join(f"{col}: {row[col]}" for col in df.columns)
                    
                    # Create metadata from all columns
                    metadata = {
                        'source_file': filename,
                        **{str(col): str(row[col]) for col in df.columns}
                    }
                    
                    all_docs.append(Document(
                        page_content=content,
                        metadata=metadata
                    ))
                
                print(f"Successfully loaded {filename}")
                
            except Exception as e:
                print(f"Error loading {filename}: {str(e)}")
                continue
    
    return all_docs