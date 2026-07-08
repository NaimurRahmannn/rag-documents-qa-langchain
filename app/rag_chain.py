from langchain_core.runnables import RunnableParallel,RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from app.retriever import get_retriever
from app.prompt import RAG_PROMPT
from app.llm import get_llm

def format_docs(docs):
    return "\n\n".join(d.page_content for d in docs)

def build_rag_chain():
    retriever=get_retriever()
    llm=get_llm()
    chain = (
        RunnableParallel({
            "docs": retriever,
            "question": RunnablePassthrough(),
        })
        | RunnablePassthrough.assign(
            context=lambda x: format_docs(x["docs"])
          )
        | RunnableParallel({
            "answer": RAG_PROMPT | llm | StrOutputParser(),
            "sources": lambda x: [
                {"source": d.metadata.get("source"), "page": d.metadata.get("page")}
                for d in x["docs"]
            ],
        })
    )
    return chain