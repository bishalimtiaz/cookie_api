from pydantic import BaseModel

from app.schemas.minerals_schema import Minerals
from app.schemas.units_schema import Units
from app.schemas.vitamins_schema import Vitamins


class FoodBase(BaseModel):
    name: str
    quantity: float
    fat: float
    protein: float
    carb: float
    fiber: float
    netCarb: float
    calories: float
    units: Units
    vitamins: Vitamins
    minerals: Minerals


class Food(FoodBase):
    pass

    class Config:
        orm_mode = True


class FoodCreate(FoodBase):
    pass


class FoodUpdate(FoodBase):
    pass
