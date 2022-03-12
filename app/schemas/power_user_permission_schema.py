from typing import List

from pydantic import BaseModel

from app.schemas import user_role_schema, power_user_schema


class PowerUserPermissionBase(BaseModel):
    power_user_id: int


class PowerUserPermissionCreate(PowerUserPermissionBase):
    user_role_ids: List[int]


class PowerUserPermissionUpdate(PowerUserPermissionBase):
    pass


class PowerUserPermission(PowerUserPermissionBase):
    user_role: user_role_schema.UserRole
    user_permission: power_user_schema.PowerUser

    class Config:
        orm_mode = True
