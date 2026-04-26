from app.schemas.equipo_schema import EquipoSchema
from app.repositories.equipo_repository import EquipoRepository
from app.repositories.cliente_repository import ClienteRepository
from sqlalchemy.orm import Session

class EquipoService:
    def __init__(self):
        self.equipo_repository = EquipoRepository()
        self.cliente_repository = ClienteRepository()

    def crear_equipo(self, peticion:EquipoSchema):
        cliente = self.cliente_repository.buscar_cliente_por_cedula(peticion.cedula_cliente)

        if not cliente:
            return {"Error": "Cliente no existe"}
        id_cliente = cliente["id"]
        nuevo_equipo = self.equipo_repository.crear_equipo_json(peticion, id_cliente)

        return {"message": "equipo creado exitosamete", "data": nuevo_equipo}
    
    def traer_equipo_por_id(self, db:Session, equipo_id:int)
        
        