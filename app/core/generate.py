from app.constants.role import Role

from app.models.roles_model import Roles
from app.secuirity.database import Session


def create_roles():
    with Session() as db:
        # db.query(UserRole).delete()
        role = db.query(Roles).first()
        if not role:
            roles = [Roles(**Role.GUEST), Roles(**Role.ADMIN), Roles(**Role.SUPER_ADMIN),
                     Roles(**Role.END_USER)]
            db.add_all(roles)
            db.commit()
