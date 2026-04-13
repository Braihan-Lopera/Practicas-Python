from app.schemas.registroReparacion_schema import RegistroReparacionSchema
from app.repositories.registro_repository import RegistroRepository
from app.repositories.tecnico_repository import TecnicoRepository



class RegistroService:
    def __init__(self):
        self.registro_repository = RegistroRepository()
        self.tecnico_repository = TecnicoRepository()
        
    def crear_registro(self, peticion:RegistroReparacionSchema):
        tecnico = self.tecnico_repository.buscar_tecnico_por_cedula(peticion.cedula_tecnico)
        
        if not tecnico:
            return {"Error": "tecnico no encontrado"}
        id_tecnico = tecnico["id"]
        nuevo_registro = self.registro_repository.crear_registro_json(peticion, id_tecnico)

        return {"message": "Registro creado correctamente", "data": nuevo_registro}