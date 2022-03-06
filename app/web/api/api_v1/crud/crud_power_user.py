from app.core.crud_base import CRUDBase
from app.models.power_user_model import PowerUser
from app.schemas.power_user_schema import PowerUserCreate, PowerUserUpdate


class CRUDPowerUser(CRUDBase[PowerUser, PowerUserCreate, PowerUserUpdate]):
    pass


power_user = CRUDPowerUser(PowerUser)
