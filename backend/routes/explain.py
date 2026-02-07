from fastapi import APIRouter
from pydantic import BaseModel
from rag.chain import get_rag_chain

router=APIRouter()
qa_chain=get_rag_chain()

class ExplainRequest(BaseModel):
    text:str

@router.post("/explain")
def explain_text(request:ExplainRequest):
    answer=qa_chain.run(request.text)
    return {
        "question":request.text,
        "explaination":answer}