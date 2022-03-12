from typing import TypeVar, Generic, Type, List

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.secuirity.database import Base

LeftModelType = TypeVar("LeftModelType", bound=Base)
RightModelType = TypeVar("RightModelType", bound=Base)


class RelationshipCRUDBase(Generic[LeftModelType, RightModelType]):
    def __init__(self, left_model: Type[LeftModelType], right_model: Type[RightModelType]):
        self.left_model = left_model
        self.right_model = right_model

    def create_one_to_many(self, db: Session, *, right_models: List[RightModelType]):
        pass
