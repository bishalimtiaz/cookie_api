from sqlalchemy.orm import Session

from app.core.crud_base import CRUDBase
from app.models import Food
from app.schemas.food_schema import FoodCreate, FoodUpdate


# .offset((page_num-1)*item_per_page).limit(item_per_page)

class CRUDFood(CRUDBase[Food, FoodCreate, FoodUpdate]):
    def search_food(self, db: Session, keyword: str, item_per_page: int, page_num: int):
        return db.query(self.model) \
            .filter(self.model.name.like('%' + keyword + '%')) \
            .order_by(self.model.name) \
            .offset((page_num - 1) * item_per_page) \
            .limit(item_per_page) \
            .all()


food = CRUDFood(Food)
