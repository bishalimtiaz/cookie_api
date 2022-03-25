from app.core.crud_base import CRUDBase
from app.models import Food
from app.schemas.food_schema import FoodCreate, FoodUpdate


class CRUDFood(CRUDBase[Food, FoodCreate, FoodUpdate]):
    pass


food = CRUDFood(Food)
