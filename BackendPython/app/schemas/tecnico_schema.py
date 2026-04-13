from pydantic import BaseModel
from datetime import date

class TecnicoSchema(BaseModel):
    nombre:str
    correo:str
    cedula:str
    fecha_nacimiento: date
    especialidad:str
    cargo:str
    