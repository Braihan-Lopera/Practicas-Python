import json
from pathlib import Path
from app.schemas.factura_schema import FacturaSchema

class FacturaRepository:
    def guardar_factura_json(self, peticion:FacturaSchema):
        ruta = Path("facturas.json")

        if ruta.exists():
            with open(ruta, "r", encoding="utf-8") as file:
                facturas = json.load(file)
        else:
            facturas = []
        
        nueva_factura = {
            "id": len(facturas) + 1,
            "subtotal": peticion.subtotal,
            "metodo_pago": peticion.metodo_pago,
            "observaciones":peticion.observaciones
        }
        facturas.append(nueva_factura)

        with open(ruta, "w") as file:
            json.dump(facturas, file, indent=4)
        return nueva_factura
    

    def buscar_factura_por_id(self, id:int):
        ruta = Path("facturas.json")

        if not ruta.exists():
            return None
        
        with open(ruta,"r", encoding="utf-8") as file:
            facturas = json.load(file)


        for registro in facturas:
            if id == registro["id"]:
                return registro 
        
        