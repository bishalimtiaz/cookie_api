from sqlalchemy import Column, String, Integer, Float, ForeignKey

from .meta import Base


class Vitamins(Base):
    __tablename__ = "vitamins"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    food_id = Column(Integer, ForeignKey('food.id'), primary_key=True)
    b1ThiamineMg = Column(Float)
    b2RiboflavinMg = Column(Float)
    b3NiacinMg = Column(Float)
    b5PantothenicAcidMg = Column(Float)
    b6PyridoxineMg = Column(Float)
    b12CobalaminMicg = Column(Float)
    b7BiotinMg = Column(Float)
    b8CholineMg = Column(Float)
    b9FolateMicg = Column(Float)
    vitaminAIU = Column(Float)
    vitaminCMg = Column(Float)
    vitaminDIU = Column(Float)
    vitaminEMg = Column(Float)
    vitaminKMicg = Column(Float)

    __mapper_args__ = {"eager_defaults": True}
