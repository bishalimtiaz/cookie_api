from fastapi import APIRouter

from app.web.api.api_v1.routers import user_role_router
from app.web.api.api_v1.routers import power_user_router
from app.web.api.api_v1.routers import power_user_permission_router
from app.web.api.api_v1.routers import authentication_router

api_router = APIRouter(
    prefix='/web/api/v1'
)

api_router.include_router(user_role_router.router)
api_router.include_router(power_user_router.router)
api_router.include_router(power_user_permission_router.router)
api_router.include_router(authentication_router.router)
