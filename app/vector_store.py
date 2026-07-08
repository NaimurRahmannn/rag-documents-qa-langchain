from langchain_chroma import Chroma
from app.embeddings import get_embeddings
from app.config import CHROMA_PERSIST_DIR

def get_vector_store():
    return Chroma(
        collection_name="rag_documents",
        embedding_function=get_embeddings(),
        persist_directory=CHROMA_PERSIST_DIR
    )
def add_documents(chunks):
    store=get_vector_store()
    store.add_documents(chunks)
    return store