from pydantic import BaseModel


class UnitBase(BaseModel):
    unit_name: str
    unit_symbol: str = None
    unit_category: str = None


class Unit(UnitBase):
    pass

    class Config:
        orm_mode = True


class UnitCreate(UnitBase):
    pass


class UnitUpdate(UnitBase):
    pass
