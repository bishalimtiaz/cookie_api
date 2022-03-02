from sqlalchemy import delete

from app.constants.role import Role
from app.models import UserRole
from app.secuirity.database import async_session, engine


async def create_roles():
    async with async_session() as db:
        await db.execute(delete(UserRole))
        roles = [UserRole(**Role.GUEST), UserRole(**Role.ADMIN), UserRole(**Role.SUPER_ADMIN),
                 UserRole(**Role.END_USER)]
        # db.add(UserRole(**Role.GUEST))
        db.add_all(roles)
        await db.commit()
