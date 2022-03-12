from app.core.crud_base import CRUDBase
from app.models.power_user_role_model import PowerUserRole
from app.schemas.power_user_permission_schema import PowerUserPermissionCreate, PowerUserPermissionUpdate


class CRUDPowerUserPermission(CRUDBase[PowerUserRole, PowerUserPermissionCreate, PowerUserPermissionUpdate]):
    pass


power_user_permission = CRUDPowerUserPermission(PowerUserRole)
