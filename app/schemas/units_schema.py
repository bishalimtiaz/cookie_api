from pydantic import BaseModel


class UnitsBase(BaseModel):
    unit_name: str
    unit_symbol: str = None
    unit_category: str = None


class Units(UnitsBase):
    pass

    class Config:
        orm_mode = True


class UnitsCreate(UnitsBase):
    pass


class UnitsUpdate(UnitsBase):
    pass
