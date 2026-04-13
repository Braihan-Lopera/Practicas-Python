from app.services.tecnico_service import TecnicoService
from app.schemas.tecnico_schema import TecnicoSchema
from fastapi import APIRouter

router = APIRouter()
tecnico_service = TecnicoService()
@router.post("/tecnico")
def crear_tecnico(peticion:TecnicoSchema):
    return tecnico_service.crear_tecnico(peticion)