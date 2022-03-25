from fastapi import APIRouter
from app.mobile.api.api_v1.routers import food_router

api_router = APIRouter(
    prefix='/mobile/api/v1'
)

api_router.include_router(food_router.router)


