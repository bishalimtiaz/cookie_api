from pydantic import BaseModel


# Shared properties
class UserRoleBase(BaseModel):
    name: str
    description: str


# Properties to share with user
class UserRole(UserRoleBase):
    pass

    class Config:
        orm_mode = True


# Properties to receive on item creation
class UserRoleCreate(UserRoleBase):
    pass


# Properties to receive on item update
class UserRoleUpdate(UserRoleBase):
    pass
