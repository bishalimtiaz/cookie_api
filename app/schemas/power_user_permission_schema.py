from pydantic import BaseModel
import power_user_schema
import user_role_schema


class PowerUserPermissionBase(BaseModel):
    power_user_id: int
    user_role_id: int


class PowerUserPermissionCreate(PowerUserPermissionBase):
    pass


class PowerUserPermission(PowerUserPermissionBase):
    user_role: user_role_schema.UserRole
    user_permission: power_user_schema.PowerUser

    class Config:
        orm_mode = True
