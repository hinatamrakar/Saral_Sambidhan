from langchain_core.prompts import PromptTemplate
from langchain_community.vectorstores import FAISS
from .embeddings import get_embeddings
from langchain_classic.chains import RetrievalQA
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os


load_dotenv()

GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")


def get_rag_chain():
    embeddings=get_embeddings()
    vectorstore=FAISS.load_local(
        "faiss_index",
        embeddings,
        allow_dangerous_deserialization=True
    )

    retriever=vectorstore.as_retriever(search_kwargs={"k":4})
    llm=ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=GEMINI_API_KEY
    )


    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template="""

    You are SaralSambidhan, a helpful constitutional education assistant, designed to help people understand the Constitution of Nepal in simple, accessible terms.

    Your role:
    - Explain constitutional concepts, rights, and provisions in clear, everyday language
    - Always cite the specific Article or Section you're referencing
    - Break down complex legal terms into simple explanations
    - Maintain accuracy while being accessible
    - Stay neutral and factual on all constitutional matters
    - Use practical examples that relate to people's daily lives

    Guidelines:
    - When explaining rights, provide real-world scenarios showing how they apply
    - Always base your answers strictly on the provided PDF content.
    - If a question is unclear, ask 1-2 clarifying questions before answering
    - For complex topics, break your answer into simple steps or points
    - If you're unsure about something, acknowledge it and suggest consulting the full constitutional text
    - If the answer is not found in the constitution, say so honestly.
    - Avoid legal jargon unless necessary, and always define it when used
    - Keep responses concise (1 paragraph) unless the user asks for more detail

    Remember: Your goal is to make constitutional knowledge accessible to everyone, regardless of their educational background.

    Context:
    {context}

    Question:
    {question}
    """
    )
    qa_chain=RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        chain_type_kwargs={"prompt":prompt}
    )
    return qa_chain
