import json
import os

DATA_PATH = "data/aiko_dados.json"
DATA_USERS = "data/usuarios.json" 

def carregar_dados():
    if not os.path.exists(DATA_PATH):
        return {"respostas": {}}

    try:
        with open(DATA_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {"respostas": {}}
    if not os.path.exists(DATA_USERS):
        return {}
    try:
        with open(DATA_USERS, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}