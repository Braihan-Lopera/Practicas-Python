from fastapi import APIRouter
from app.schemas.cliente_schema import ClienteSchema
from app.services.cliente_service import ClienteService



router = APIRouter()
cliente_service = ClienteService()

@router.post("/clientes")
def crear_cliente(peticion:ClienteSchema):
    return cliente_service.crear_cliente(peticion)

