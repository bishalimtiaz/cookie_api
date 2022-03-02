from typing import List

from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.schemas import user_role_schema
from app.secuirity.database import get_db
from app.web.api.api_v1.crud import crud_user_role as crud

router = APIRouter(
    prefix='/role',
    tags=["Web/user_role"]
)


@router.post('/')
def create_user_role(request_user_role: user_role_schema.UserRoleCreate, db: Session = Depends(get_db)):
    return crud.user_role.create(db=db, obj_in=request_user_role)


@router.get('/{id}', response_model=user_role_schema.UserRole)
def get_user_role(id: int, db: Session = Depends(get_db), ):
    return crud.user_role.get(db, id=id)


@router.get('/', response_model=List[user_role_schema.UserRole])
def get_user_roles(db: Session = Depends(get_db), ):
    return crud.user_role.get_multi(db)

# @router.get('/')
# def get_user_role(
#         db: Session = Depends(get_db),
#         current_user: power_user_schema.ShowPowerUser = Security(
#             get_current_user,
#             scopes=[Role.ADMIN["name"], Role.SUPER_ADMIN["name"]],
#         ),
#
# ):
#     return user_role_repo.get_user_role(db)
