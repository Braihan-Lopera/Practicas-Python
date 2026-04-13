from app.schemas.registroReparacion_schema import RegistroReparacionSchema
import json
from pathlib import Path


class RegistroRepository:
    def crear_registro_json(self, peticion:RegistroReparacionSchema, id_tecnico:str):
        ruta = Path("registros.json")

        if not ruta.exists():
            with open(ruta, "r", encoding="utf-8") as file:
                registros = json.load(file)
        else:
            registros = []

        nuevo_registro = {
            "id":len(registros) + 1,
            "observaciones": peticion.observaciones,
            "detalles": peticion.detalles,
            "motivo_reparacion": peticion.motivo_reparacion,
            "id_tecnico": id_tecnico,
            "nro_serie": peticion.nro_serie_equipo
        }

        registros.append(nuevo_registro)