from sqlalchemy import Column, String, Integer, Float, ForeignKey

from .meta import Base


class Minerals(Base):
    __tablename__ = "minerals"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    food_id = Column(Integer, ForeignKey('food.id'), primary_key=True)
    calciumMg = Column(Float)
    copperMg = Column(Float)
    ironMg = Column(Float)
    magnesiumMg = Column(Float)
    manganeseMg = Column(Float)
    phosphosusMg = Column(Float)
    potassiumMgval = Column(Float)
    seleniumMicg = Column(Float)
    sodiumMg = Column(Float)
    zincMg = Column(Float)

    __mapper_args__ = {"eager_defaults": True}
