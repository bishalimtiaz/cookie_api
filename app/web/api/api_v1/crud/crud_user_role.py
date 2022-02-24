from app.core.crud_base import CRUDBase
from app.schemas.user_role_schema import UserRoleCreate, UserRoleUpdate
from app.models.user_role_model import UserRole


class CRUDUserROle(CRUDBase[UserRole, UserRoleCreate, UserRoleUpdate]):
    pass


user_role = CRUDUserROle(UserRole)
