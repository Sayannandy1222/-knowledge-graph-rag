from fastapi import APIRouter
from pydantic import BaseModel

from app.retrieval.hybrid_search import hybrid_search
from app.llm.rag import generate_answer

router = APIRouter()


class ChatRequest(BaseModel):
    question: str


@router.post("/chat")
def chat(request: ChatRequest):

    context = hybrid_search(request.question)

    answer = generate_answer(
        request.question,
        context,
    )

    return {
        "question": request.question,
        "answer": answer,
    }