from fastapi import APIRouter, Depends, status
from app.schemas.power_user_schema import PowerUserCreate
from sqlalchemy.orm import Session
from app.secuirity.database import get_db
from app.web.api.api_v1.repositories import power_user_repo as repo


router = APIRouter(
    prefix='/power_user',
    tags=["Web/power_user"]
)


# create power user
@router.post('/', status_code=status.HTTP_201_CREATED)
def create_power_user(power_user: PowerUserCreate, db: Session = Depends(get_db)):
    return repo.create_power_user(db=db, power_user=power_user)

# # fetch power user
# @router.get('/', status_code=status.HTTP_200_OK)
# def fetch_power_user(id, db: Session = Depends(get_db)):
#     return power_user_repo.fetch_power_user(id, db)
