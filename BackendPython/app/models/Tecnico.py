from dataclasses import dataclass
from datetime import datetime, date


@dataclass
class Tecnico:
    id:int
    nombre:str
    correo:str
    cedula:str
    fecha_nacimiento: date
    fecha_ingreso: datetime
    tipo_contrato:str #luego se relacionara con una entidad contrato
    cargo:str
    especialidad:str

