from fastapi import APIRouter

api_router = APIRouter(
    prefix='/web/api/v1'
)


@api_router.get('/')
def web():
    return "web"
