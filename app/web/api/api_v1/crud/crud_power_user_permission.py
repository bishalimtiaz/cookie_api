from app.core.crud_base import CRUDBase
from app.models.power_user_permission_model import PowerUserPermission
from app.schemas.power_user_permission_schema import PowerUserPermissionCreate, PowerUserPermissionUpdate


class CRUDPowerUserPermission(CRUDBase[PowerUserPermission, PowerUserPermissionCreate, PowerUserPermissionUpdate]):
    pass


power_user_permission = CRUDPowerUserPermission(PowerUserPermission)
