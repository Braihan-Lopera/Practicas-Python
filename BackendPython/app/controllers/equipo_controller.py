from fastapi import APIRouter
from app.schemas.equipo_schema import EquipoSchema
from app.services.equipo_service import EquipoService

router = APIRouter()
equipo_service = EquipoService()

@router.post("/equipo")
def crear_equipo(peticion:EquipoSchema):
    return equipo_service.crear_equipo(peticion)
