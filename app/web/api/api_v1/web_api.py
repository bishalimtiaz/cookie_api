from fastapi import APIRouter

from app.web.api.api_v1.routers import user_role_router

api_router = APIRouter(
    prefix='/web/api/v1'
)


api_router.include_router(user_role_router.router)
