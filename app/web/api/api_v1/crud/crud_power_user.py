from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from app.core.crud_base import CRUDBase
from app.models.power_user_model import PowerUser
from app.schemas.power_user_schema import PowerUserCreate, PowerUserUpdate, PowerUserAuthenticate
from app.secuirity.hashing import Hash
from app.secuirity.jwt_token import create_access_token


class CRUDPowerUser(CRUDBase[PowerUser, PowerUserCreate, PowerUserUpdate]):
    def authenticate(self, db: Session, *, user: PowerUserAuthenticate):
        power_user = db.query(self.model).filter(self.model.email == user.email).first()
        if not power_user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Invalid Credentials")
        if not Hash.verify(power_user.password, user.password):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Wrong Password")
        if not power_user.roles:
            role = "GUEST"
        else:
            role = power_user.roles.user_role.name
        token_payload = {
            "id": str(power_user.id),
            "role": role,
        }
        access_token = create_access_token(
            data=token_payload
        )
        return {"access_token": access_token, "token_type": "bearer"}


power_user = CRUDPowerUser(PowerUser)
