import datetime

from sqlalchemy import Column, String, Integer, TEXT, Boolean, DateTime
from .meta import Base
from sqlalchemy.orm import relationship


class PowerUser(Base):
    __tablename__ = "power_user"

    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String(16))
    email = Column(TEXT)
    password = Column(TEXT)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    updated_at = Column(DateTime, default=datetime.datetime.utcnow(), onupdate=datetime.datetime.utcnow())
    roles = relationship("PowerUserPermission", back_populates="user_permission", uselist=False)

    __mapper_args__ = {"eager_defaults": True}
