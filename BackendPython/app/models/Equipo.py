from dataclasses import dataclass


@dataclass
class Equipo:
    id:int
    marca:str
    modelo:str
    nro_serie:str
    id_cliente:int