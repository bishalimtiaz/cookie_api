from pydantic import BaseModel


class VitaminsBase(BaseModel):
    b1ThiamineMg: float
    b2RiboflavinMg: float
    b3NiacinMg: float
    b5PantothenicAcidMg: float
    b6PyridoxineMg: float
    b12CobalaminMicg: float
    b7BiotinMg: float
    b8CholineMg: float
    b9FolateMicg: float
    vitaminAIU: float
    vitaminCMg: float
    vitaminDIU: float
    vitaminEMg: float
    vitaminKMicg: float


class Vitamins(VitaminsBase):
    pass

    class Config:
        orm_mode = True


class VitaminsCreate(VitaminsBase):
    pass


class VitaminsUpdate(VitaminsBase):
    pass
