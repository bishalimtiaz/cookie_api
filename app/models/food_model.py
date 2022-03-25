from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

from .meta import Base


class Food(Base):
    __tablename__ = "food"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(32))
    quantity = Column(Float)
    unit_id = Column(Integer, ForeignKey('units.id'))
    fat = Column(Float)
    protein = Column(Float)
    carb = Column(Float)
    fiber = Column(Float)
    netCarb = Column(Float)
    calories = Column(Float)
    units = relationship('Units', uselist=False)
    vitamins = relationship('Vitamins', uselist=False)
    minerals = relationship('Minerals', uselist=False)

    __mapper_args__ = {"eager_defaults": True}
