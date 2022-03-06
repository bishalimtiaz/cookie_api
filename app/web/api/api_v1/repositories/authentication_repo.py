from sqlalchemy.orm import Session
from app.schemas.power_user_schema import PowerUserAuthenticate
from app.web.api.api_v1.crud import crud_power_user as crud


def login(user: PowerUserAuthenticate, db: Session):
    return crud.power_user.authenticate(db, user=user)
