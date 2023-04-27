from dotenv import load_dotenv
from pathlib import Path
dotenv_path = Path('settings/.env')
load_dotenv(dotenv_path=dotenv_path)
from llama_index import GPTSimpleVectorIndex, SimpleDirectoryReader
documents = SimpleDirectoryReader('data').load_data()
index = GPTSimpleVectorIndex.from_documents(documents)
while True : 
    prompt = input(">>")
    print(index.query(prompt))