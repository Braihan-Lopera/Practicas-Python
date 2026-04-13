from app.services.factura_service import FacturaService
from app.schemas.factura_schema import FacturaSchema
from fastapi import APIRouter

router = APIRouter()
factura_service = FacturaService()

@router.post("/factura")
def guardar_factura(peticion: FacturaSchema):
    return factura_service.guardar_factura(peticion)
     