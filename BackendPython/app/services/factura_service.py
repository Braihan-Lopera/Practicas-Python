from app.repositories.factura_repository import FacturaRepository
from app.schemas.factura_schema import FacturaSchema

class FacturaService:
    def __init__(self):
        self.factura_repository = FacturaRepository()
    
    def guardar_factura(self, peticion:FacturaSchema):
        factura_guardada = self.factura_repository.guardar_factura_json(peticion)
        return {"Message": "Factura guardada", "data": factura_guardada}