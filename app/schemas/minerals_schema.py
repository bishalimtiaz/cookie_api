from pydantic import BaseModel


class MineralsBase(BaseModel):
    calciumMg: float
    copperMg: float
    ironMg: float
    magnesiumMg: float
    manganeseMg: float
    phosphosusMg: float
    potassiumMgval: float
    seleniumMicg: float
    sodiumMg: float
    zincMg: float


class Minerals(MineralsBase):
    pass

    class Config:
        orm_mode = True


class MineralsCreate(MineralsBase):
    pass


class MineralsUpdate(MineralsBase):
    pass
