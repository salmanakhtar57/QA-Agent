from fastapi import APIRouter
from app.apis.aiagent_endpoint import router as chat_router

api_router = APIRouter()

api_router.include_router(chat_router, prefix="/ai_agent", tags=["AI Agent"])

