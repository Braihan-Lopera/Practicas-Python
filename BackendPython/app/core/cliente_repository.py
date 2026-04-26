import json
from pathlib import Path
from app.schemas.cliente_schema import ClienteSchema

class ClienteRepository:
    def crear_cliente_json(self, peticion:ClienteSchema):
        ruta = Path("clientes.json")

        if ruta.exists():
            with open(ruta, "r", encoding="utf-8") as file:
                clientes = json.load(file)
        else:
            clientes = []
        
        nuevo_cliente = {
            "id": len(clientes) + 1,
            "nombre": peticion.nombre,
            "correo": peticion.correo,
            "cedula": peticion.cedula,
            "celular":peticion.celular
        }
        clientes.append(nuevo_cliente)

        with open(ruta, "w") as file:
            json.dump(clientes, file, indent=4)

        return nuevo_cliente
    
    def buscar_cliente_por_cedula(self, cedula: str):
        ruta = Path("clientes.json")

        if not ruta.exists():
            return None
        
        with open(ruta, "r", encoding="utf-8") as file:
            clientes = json.load(file)
        
        for cliente in clientes:
            if  cedula == cliente["cedula"]:
                return cliente
        
        return None