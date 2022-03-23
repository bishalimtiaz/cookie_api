from app.constants.role import Role
from app.main import get_settings
from app.models.power_user_model import PowerUser
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


def create_super_admin():
    with Session() as db:
        power_user = db.query(PowerUser).first()
        role = db.query(Roles).filter(Roles.name == Role.ADMIN['name']).first()
        if not power_user:
            settings = get_settings()
            user = PowerUser(user_name='Super Admin', email=settings.admin_email, password=settings.admin_password)
            user.roles = [role]
            db.add(user)
            db.commit()
