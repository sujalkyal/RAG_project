# File: api/chat.py
from fastapi import APIRouter
from models.schema import ChatRequest
from services.router import route_question

router = APIRouter()

@router.post("/chat")
async def chat_endpoint(request: ChatRequest):
    response = await route_question(request)
    return {"response": response}
