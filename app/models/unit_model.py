from sqlalchemy import Column, String, Integer

from .meta import Base


class Unit(Base):
    __tablename__ = "unit"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    unit_name = Column(String(16))
    unit_symbol = Column(String(16), nullable=True)
    unit_category = Column(String(32), nullable=True)

    __mapper_args__ = {"eager_defaults": True}
