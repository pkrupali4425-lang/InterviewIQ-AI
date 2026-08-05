from langchain_chroma import Chroma

from backend.embeddings import get_embeddings


def create_vector_store(chunks):

    embeddings = get_embeddings()

    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="vectorstore"
    )

    return vectordb