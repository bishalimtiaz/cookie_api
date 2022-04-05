from sqlalchemy.orm import Session
from app.mobile.api.api_v1.crud import crud_food as crud


def get_foods(db: Session):
    return crud.food.get_multi(db=db)


def get_foods_pagging(db: Session, item_per_page: int, page_num: int):
    return crud.food.get_multi_pagging(db=db, item_per_page=item_per_page, page_num=page_num)


def search_food(db: Session, keyword: str, item_per_page: int, page_num: int):
    return crud.food.search_food(db=db, keyword=keyword, item_per_page=item_per_page, page_num=page_num)
