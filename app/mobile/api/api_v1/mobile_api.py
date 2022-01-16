from fastapi import APIRouter

api_router = APIRouter(
    prefix='/mobile/api/v1'
)


@api_router.get('/')
def mobile():
    return "mobile"
