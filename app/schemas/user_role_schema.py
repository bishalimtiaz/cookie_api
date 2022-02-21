from pydantic import BaseModel


class UserRoleBase(BaseModel):
    title: str
    description: str


class UserRole(UserRoleBase):
    class Config:
        orm_mode = True
