from app.vector_store import get_vector_store
from app.config import TOP_K

def get_retriever():
    store=get_vector_store()
    return store.as_retriever(search_kwargs={"k":TOP_K})