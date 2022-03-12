from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from .meta import Base


class PowerUserRole(Base):
    __tablename__ = "power_user_role"

    power_user_id = Column(Integer, ForeignKey('power_user.id'), primary_key=True)
    user_role_id = Column(Integer, ForeignKey('roles.id'), primary_key=True)

    __mapper_args__ = {"eager_defaults": True}
