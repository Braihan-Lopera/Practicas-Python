from dataclasses import dataclass
from datetime import datetime

@dataclass
class Factura:
    id:int
    fecha_expedicion:datetime
    subtotal:float
    metodo_pago:str
    pagada:bool
    id_registro:int
    observaciones:str
