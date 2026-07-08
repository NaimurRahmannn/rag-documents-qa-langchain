# tests/test_chain.py
from app.rag_chain import build_rag_chain

def test_rag_chain_returns_answer_and_sources():
    chain = build_rag_chain()
    result = chain.invoke("What is this document about?")
    assert "answer" in result
    assert "sources" in result
    assert isinstance(result["sources"], list)