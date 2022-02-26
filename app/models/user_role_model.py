from sqlalchemy import Column, String, Integer, TEXT

from .meta import Base


class UserRole(Base):
    __tablename__ = "user_role"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(16))
    description = Column(TEXT)

    # required in order to access columns with server defaults
    # or SQL expression defaults, subsequent to a flush, without
    # triggering an expired load
    __mapper_args__ = {"eager_defaults": True}
