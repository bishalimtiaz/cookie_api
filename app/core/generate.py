from app.constants.role import Role

from app.models.user_role_model import UserRole
from app.secuirity.database import Session


def create_roles():
    with Session() as db:
        db.query(UserRole).delete()
        roles = [UserRole(**Role.GUEST), UserRole(**Role.ADMIN), UserRole(**Role.SUPER_ADMIN),
                 UserRole(**Role.END_USER)]
        db.add_all(roles)
        db.commit()
