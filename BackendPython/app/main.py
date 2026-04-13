from fastapi import FastAPI
from app.controllers.cliente_controller import router as cliente_router
from app.controllers.equipo_controller import router as equipo_router
from app.controllers.tecnico_controller import router as tecnico_router
from app.controllers.factura_controller import router as factura_router

app = FastAPI()
app.include_router(cliente_router)
app.include_router(equipo_router)
app.include_router(tecnico_router)
app.include_router(factura_router)

@app.get("/")
def root():
    return {"message": "API is running :D"}