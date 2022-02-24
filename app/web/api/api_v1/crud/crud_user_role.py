from app.core.crud_base import CRUDBase
from app.schemas.user_role_schema import *
from app.models import UserRole


class CRUDUserROle(CRUDBase[UserRole, UserRoleCreate, UserRoleUpdate]):
    pass
