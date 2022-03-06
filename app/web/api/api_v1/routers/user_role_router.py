from typing import List

from fastapi import APIRouter, Security
from fastapi import Depends
from sqlalchemy.orm import Session

from app.constants.role import Role
from app.schemas.user_role_schema import UserRoleCreate, UserRole
from app.secuirity.database import get_db
from app.secuirity.oauth2 import get_current_user
from app.web.api.api_v1.repositories import user_role_repo as repo

router = APIRouter(
    prefix='/role',
    tags=["Web/user_role"]
)


@router.post('/')
def create_user_role(user_role: UserRoleCreate, db: Session = Depends(get_db)):
    return repo.create_user_role(db=db, user_role=user_role)


@router.get('/{id}', response_model=UserRole)
def get_user_role(id: int, db: Session = Depends(get_db)):
    return repo.get_user_role(db=db, id=id)


@router.get('/', response_model=List[UserRole])
def get_user_roles(
        db: Session = Depends(get_db),
        current_user: UserRole = Security(
            get_current_user,
            scopes=[Role.ADMIN["name"], Role.SUPER_ADMIN["name"]],
        ),
):
    return repo.get_user_roles(db)
