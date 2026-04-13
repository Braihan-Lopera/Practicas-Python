from dataclasses import dataclass
from datetime import datetime

@dataclass
class RegistroReparacion:
    id:int
    estado:str
    fecha_ingreso:datetime
    observaciones:str
    detalles:str
    motivo_reparacion:str
    id_tecnico:int
    id_equipo:int