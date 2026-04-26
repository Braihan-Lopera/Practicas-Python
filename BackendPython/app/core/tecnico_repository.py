import json
from pathlib import Path
from app.schemas.tecnico_schema import TecnicoSchema

class TecnicoRepository:
    def crear_tecnico_json(self, peticion:TecnicoSchema):
        ruta = Path("tecnicos.json")

        if ruta.exists():
            with open(ruta, "r", encoding="utf-8") as file:
                tecnicos = json.load(file)
        else:
            tecnicos = []
        
        nuevo_tecnico = {
            "id": len(tecnicos) + 1,
            "nombre": peticion.nombre,
            "correo":peticion.correo,
            "cedula":peticion.cedula,
            "fecha_nacimiento": str(peticion.fecha_nacimiento), #fechas pasarlas a str para que json no lance 500 o 422
            "especialidad":peticion.especialidad,
            "cargo":peticion.cargo
        }
        tecnicos.append(nuevo_tecnico)

        with open(ruta, "w") as file:
            json.dump(tecnicos, file, indent=4)
        return nuevo_tecnico
    def buscar_tecnico_por_cedula(cedula:str):
        ruta = Path("tecnicos.json")
        if ruta.exists():
            with open(ruta, "r", encoding="utf-8") as file:
                tecnicos = json.load(file)
        else:
            tecnicos = []

        for tecnico in tecnicos:
            if cedula == tecnico["cedula"]:
                return tecnico