from app.core.crud_base import CRUDBase
from app.schemas.user_role_schema import UserRoleCreate, UserRoleUpdate
from app.models.roles_model import Roles


class CRUDUserROle(CRUDBase[Roles, UserRoleCreate, UserRoleUpdate]):
    pass


user_role = CRUDUserROle(Roles)
