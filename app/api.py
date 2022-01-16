from fastapi import APIRouter
from app.web.api.api_v1 import web_api
from app.mobile.api.api_v1 import mobile_api

api_router = APIRouter()

api_router.include_router(web_api.api_router)
api_router.include_router(mobile_api.api_router)
