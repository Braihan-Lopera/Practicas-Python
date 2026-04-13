from pydantic import BaseModel
from datetime import date

class ClienteSchema(BaseModel): # <- BaseModel convierte los datos en un schema o formato json
    nombre: str
    correo: str
    cedula: str
    celular: str
    ciudad: str
    barrio: str
    direccion: str
    fecha_nacimiento: date