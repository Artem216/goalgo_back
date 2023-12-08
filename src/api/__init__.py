from fastapi import APIRouter
from src.user.endpoints import router as user_router
from src.trader.endpoints import router as trader_router
from src.bot.endpoints import router as bot_router

api_router = APIRouter(prefix="/api/v1")

api_router.include_router(user_router)
api_router.include_router(trader_router)
api_router.include_router(bot_router)
