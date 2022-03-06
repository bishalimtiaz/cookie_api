# create power user
from sqlalchemy.orm import Session
from app.schemas.power_user_schema import PowerUserCreate
from app.web.api.api_v1.crud import crud_power_user as crud
from app.secuirity.hashing import Hash


def create_power_user(db: Session, power_user: PowerUserCreate):
    power_user.password = Hash.encrypt(power_user.password)
    return crud.power_user.create(db, obj_in=power_user)
