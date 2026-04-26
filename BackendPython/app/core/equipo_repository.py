import json
from pathlib import Path
from app.schemas.equipo_schema import EquipoSchema

class EquipoRepository:
    def crear_equipo_json(self, peticion:EquipoSchema, id_cliente):
        ruta = Path("equipos.json")

        if ruta.exists():
            with open(ruta, "r", encoding="utf-8") as file:
                equipos = json.load(file)    
        else:
            equipos = []

        nuevo_equipo = {
            "id": len(equipos) + 1,
            "marca": peticion.marca,
            "modelo": peticion.modelo,
            "nro_serie": peticion.nro_serie,
            "id_cliente": id_cliente
        }

        equipos.append(nuevo_equipo)

        with open(ruta, "w") as file:
            json.dump(equipos, file, indent=4)
        return nuevo_equipo

    def traer_equipo_por_id(self, )
    