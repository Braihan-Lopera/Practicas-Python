import json
from pathlib import Path


def conection():
    ruta = Path("equipos.json")
    if ruta.exists():
        with open(ruta, encoding="utf-8") as file:
            return son.load(file)
    else:
        return []