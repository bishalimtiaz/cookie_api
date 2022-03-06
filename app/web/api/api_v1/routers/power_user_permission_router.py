from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from app.schemas.power_user_permission_schema import PowerUserPermissionCreate
from app.secuirity.database import get_db
from app.web.api.api_v1.repositories import powe_user_permission_repo as repo

router = APIRouter(
    prefix='/power_user/permission',
    tags=["Web/power_user_permission"]
)


# assign permission to a power user
@router.post('/', status_code=status.HTTP_201_CREATED)
def create_power_user_permission(
        power_user_permission: PowerUserPermissionCreate,
        db: Session = Depends(get_db)
):
    return repo.create_power_user_permission(db=db, power_user_permission=power_user_permission)

# check permissions given a user
# @router.get('/', status_code=status.HTTP_200_OK, response_model=power_user_permission_schema.ShowPowerUserPermission)
# def fetch_Permissions(
#         id,
#         db: Session = Depends(get_db)
# ):
#     return power_user_permission_repo.fetch_Permissions(id, db)
