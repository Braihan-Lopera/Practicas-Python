from pydantic import BaseModel

class RegistroReparacionSchema(BaseModel):
    observaciones:str
    detalles:str
    motivo_reparacion:str
    cedula_tecnico:str
    nro_serie_equipo:str
    