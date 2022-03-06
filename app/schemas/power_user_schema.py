from pydantic import BaseModel


class PowerUserBase(BaseModel):
    user_name: str
    email: str


class PowerUser(PowerUserBase):
    pass

    class Config:
        orm_mode = True


class PowerUserCreate(PowerUserBase):
    password: str


class PowerUserUpdate(PowerUserBase):
    pass


class PowerUserAuthenticate(BaseModel):
    email: str
    password: str
