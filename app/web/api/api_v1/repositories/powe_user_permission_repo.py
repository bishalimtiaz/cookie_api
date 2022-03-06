from sqlalchemy.orm import Session

from app.web.api.api_v1.crud import crud_power_user_permission as crud
from app.schemas.power_user_permission_schema import PowerUserPermissionCreate


def create_power_user_permission(power_user_permission: PowerUserPermissionCreate, db: Session):
    return crud.power_user_permission.create(db,obj_in=power_user_permission)
