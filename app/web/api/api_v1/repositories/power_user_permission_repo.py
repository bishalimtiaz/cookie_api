from sqlalchemy.orm import Session

from app.models import Roles
from app.web.api.api_v1.crud import crud_power_user, crud_user_role
from app.schemas.power_user_permission_schema import PowerUserPermissionCreate


def create_power_user_permission(obj_in: PowerUserPermissionCreate, db: Session):
    power_user = crud_power_user.power_user.get(db, id=obj_in.power_user_id)
    power_user.roles.clear()
    roles = crud_user_role.user_role.get_all(db, ids=obj_in.user_role_ids)
    power_user.roles.extend(roles)
    db.add(power_user)
    db.commit()
    db.refresh(power_user)
    return power_user

