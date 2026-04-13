from dataclasses import dataclass
from datetime import date

@dataclass
class Cliente:
    id:int
    nombre:str
    correo:str
    cedula:str
    celular:str
    ciudad:str
    barrio:str
    direccion:str
    fecha_nacimiento: date
    celular_secundario:str | None = None