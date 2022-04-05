from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.food_schema import Food
from app.secuirity.database import get_db
from app.mobile.api.api_v1.repositories import food_repo as repo

router = APIRouter(
    prefix='/food',
    tags=["Mobile/Food"]
)


@router.get('/all/', response_model=List[Food])
def get_foods(
        db: Session = Depends(get_db),
):
    return repo.get_foods(db)


@router.get('/', response_model=List[Food])
def get_foods_pagging(
        item_per_page: int,
        page_num: int,
        db: Session = Depends(get_db),

):
    return repo.get_foods_pagging(db=db, item_per_page=item_per_page, page_num=page_num)


@router.get('/search/{keyword}', response_model=List[Food])
def search_foods(
        keyword: str,
        item_per_page: int,
        page_num: int,
        db: Session = Depends(get_db),
):
    return repo.search_food(db=db, keyword=keyword, item_per_page=item_per_page, page_num=page_num)
