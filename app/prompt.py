from langchain_core.prompts import ChatPromptTemplate

RAG_PROMPT = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant. Answer ONLY using the provided context. "
            "If the answer isn't in the context, say you don't know. Do not make things up.",
        ),
        ("human", "Context:\n{context}\n\nQuestion: {question}"),
    ]
)
