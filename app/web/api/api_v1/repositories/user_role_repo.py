from sqlalchemy.orm import Session

from app.schemas import user_role_schema
from app.web.api.api_v1.crud import crud_user_role as crud


def create_user_role(user_role: user_role_schema.UserRoleCreate, db: Session):
    return crud.user_role.create(db=db, obj_in=user_role)


def get_user_role(db: Session,id: int):
    return crud.user_role.get(db, id=id)


def get_user_roles(db: Session):
    return crud.user_role.get_multi(db)
