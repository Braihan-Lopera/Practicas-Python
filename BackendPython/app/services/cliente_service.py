from app.schemas.cliente_schema import ClienteSchema
from app.repositories.cliente_repository import ClienteRepository

class ClienteService:
    def __init__(self):
        self.repositorio_cliente = ClienteRepository()
        pass
    def crear_cliente(self, peticion:ClienteSchema):
        nuevo_cliente = self.repositorio_cliente.crear_cliente_json(peticion)
        return {"message": "cliente creado exitosamente",
                "data": nuevo_cliente
                }

        