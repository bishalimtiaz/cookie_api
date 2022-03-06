from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.power_user_schema import PowerUserAuthenticate
from app.secuirity.database import get_db
from app.web.api.api_v1.repositories import authentication_repo as repo

router = APIRouter(
    prefix='/auth',
    tags=["Web/auth"]
)


@router.post('/')
def login(user: PowerUserAuthenticate, db: Session = Depends(get_db)):
    return repo.login(db=db, user=user)
