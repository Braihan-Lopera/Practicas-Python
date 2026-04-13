from app.repositories.tecnico_repository import TecnicoRepository
from app.schemas.tecnico_schema import TecnicoSchema

class TecnicoService:
    def __init__(self):
        self.tecnico_repository = TecnicoRepository()
    
    def crear_tecnico(self, peticion:TecnicoSchema):
        nuevo_tecnico =self.tecnico_repository.crear_tecnico_json(peticion)
        return {"Message":"Nuevo tecnico añadido", "data": nuevo_tecnico}