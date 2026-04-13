from pydantic import BaseModel


class EquipoSchema(BaseModel):
    marca:str
    modelo:str
    nro_serie:str
    cedula_cliente:str