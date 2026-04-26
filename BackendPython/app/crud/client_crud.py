from app.config.database import conection
from app.models.client import Client

class ClientCrud:
    def __init__(self):
        self.database = conection()

    def create(self, client_data:dict):
        self.database.append(client_data)
        return client_data
        

    def read(self, id:int):
        for registry in self.database:
            if id == registry["id"]:
                return registry
        return None


    def updtate(self,id:int, new_data:dict):
        for registry in self.database:
            if id == registry["id"]:
                registry.update(new_data)
                return registry
        return None

    def delete(self, id:int):
        for registry in self.database:
            if id == registry["id"]:
                self.database.remove(registry)
                return True
        return False