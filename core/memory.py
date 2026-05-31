# memory.py
# Módulo responsável por gerenciar a memória do chatbot, incluindo o armazenamento e recuperação de
# perguntas e respostas, bem como o gerenciamento de dados dos usuários. Ele fornece funções para
# carregar e salvar a memória em arquivos JSON, além de permitir que o chatbot aprenda novas
# respostas com base nas interações com os usuários. Este módulo é essencial para garantir que o
# chatbot possa evoluir e se adaptar às necessidades dos usuários ao longo do tempo, mantendo um
# registro organizado de suas interações e aprendizados.


import json
import os
import time

ultimo_input = time.time()

DATA_PATH = "data/aiko_dados.json"
DATA_USERS_DIR = "data/users"
DATA_USERNAME = "data/{username}.json"
# cria pasta automaticamente
os.makedirs(DATA_USERS_DIR, exist_ok=True)

# Função para obter o caminho do arquivo de um usuário específico
def get_user_path(username):
    return f"{DATA_USERS_DIR}/{username}.json"



# Função para carregar um arquivo JSON, retornando um dicionário vazio se o arquivo não existir ou estiver corrompido
def load_json(path):
    if not os.path.exists(path):
        return {}

    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    except Exception:
        return {}

# Função para salvar um dicionário em um arquivo JSON, lidando com erros de escrita
def save_json(path, data):
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    except Exception as e:
        print(f"Erro ao salvar JSON: {e}")

# Função para ensinar o chatbot a responder a uma nova pergunta, atualizando a memória e salvando no arquivo
def ensinar(pergunta, resposta, state, path):
    pergunta = pergunta.lower().strip()

    if pergunta not in state.respostas:
        state.respostas[pergunta] = []

    state.respostas[pergunta].append(resposta)

    save_json(path, {
        "respostas": state.respostas
    })

# Função para salvar os dados de um usuário, criando um arquivo JSON específico para cada usuário
def save_usuario(usuario):
    path = get_user_path(usuario["username"])
    save_json(path, usuario)

# Função para carregar os dados de um usuário específico, retornando um dicionário vazio se o usuário não existir
def carregar_usuario(username):
    path = get_user_path(username)
    return load_json(path)

# Função para carregar os dados gerais do chatbot, incluindo perguntas e respostas, retornando um dicionário com a estrutura esperada
def carregar_dados():
    if not os.path.exists(DATA_PATH):
        return {"respostas": {}}

    try:
        with open(DATA_PATH, "r", encoding="utf-8") as f:
            return json.load(f)

    except Exception:
        return {"respostas": {}}
