from services.storage import save_json

def ensinar(pergunta, resposta, state, path):
    pergunta = pergunta.lower().strip()

    if pergunta not in state.respostas:
        state.respostas[pergunta] = []

    state.respostas[pergunta].append(resposta)

    save_json(path, {
        "respostas": state.respostas
    })