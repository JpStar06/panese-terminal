import json
import os

DATA_PATH = "data/aiko_dados.json"
DATA_USERS = "data/usuarios.json" 

def ensinar(pergunta, resposta, state, path):
    pergunta = pergunta.lower().strip()

    if pergunta not in state.respostas:
        state.respostas[pergunta] = []

    state.respostas[pergunta].append(resposta)

    save_json(path, {
        "respostas": state.respostas
    })


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
