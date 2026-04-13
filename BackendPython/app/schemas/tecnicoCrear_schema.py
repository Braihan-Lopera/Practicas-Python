from pydantic import BaseModel
from datetime import date

class TecnicoCrearSchema(BaseModel):
    nombre: str
    correo: str
    cedula: str
    fecha_nacimiento: date
    especialidad: str
    cargo: str