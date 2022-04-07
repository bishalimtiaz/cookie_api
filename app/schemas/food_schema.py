from pydantic import BaseModel

from app.schemas.minerals_schema import Minerals
from app.schemas.unit_schema import Unit
from app.schemas.vitamins_schema import Vitamins


class FoodBase(BaseModel):
    name: str
    quantity: float
    # fat: float
    # protein: float
    # carb: float
    # fiber: float
    # netCarb: float
    calories: float
    unit: Unit
    # vitamins: Vitamins
    # minerals: Minerals


class Food(FoodBase):
    id: int
    pass

    class Config:
        orm_mode = True


class FoodCreate(FoodBase):
    pass


class FoodUpdate(FoodBase):
    pass
