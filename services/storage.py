from services.data import DATA_PATH, DATA_USERS

import json
import os

def load_json(path):
    # se não existir, retorna vazio
    if not os.path.exists(path):
        return {}

    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        # se der erro (arquivo corrompido, vazio, etc)
        return {}


def save_json(path, data):
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"Erro ao salvar JSON: {e}")

def save_usuarios(usuarios):#salva os dados da sessão anterior como cores e nomes dos usuários
    try:
        with open(DATA_USERS, "w", encoding="utf-8") as f:
            json.dump(usuarios, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"Erro ao salvar usuários: {e}")
