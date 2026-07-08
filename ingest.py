# ingest.py
from app.loader import load_directory
from app.splitter import split_documents
from app.vector_store import add_documents

if __name__ == "__main__":
    docs = load_directory("data/")
    chunks = split_documents(docs)
    add_documents(chunks)
    print(f"Indexed {len(chunks)} chunks from {len(docs)} documents.")