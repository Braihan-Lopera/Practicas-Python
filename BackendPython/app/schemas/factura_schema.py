from pydantic import BaseModel


class FacturaSchema(BaseModel):
    subtotal:float
    metodo_pago:str
    observaciones:str