from sqlalchemy import Column, String, Integer, TEXT

from .meta import Base


class Roles(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(16))
    description = Column(TEXT)

    # required in order to access columns with server defaults
    # or SQL expression defaults, subsequent to a flush, without
    # triggering an expired load
    __mapper_args__ = {"eager_defaults": True}
