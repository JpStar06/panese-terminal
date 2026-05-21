import random
from difflib import SequenceMatcher

def escolher_resposta(resp):
    if isinstance(resp, list):
        return random.choice(resp)
    return resp


def encontrar_resposta(pergunta, respostas):
    pergunta = pergunta.lower()

    melhor = None
    maior_sim = 0

    for padrao in respostas:
        sim = SequenceMatcher(None, pergunta, padrao).ratio()
        if sim > maior_sim:
            melhor = padrao
            maior_sim = sim

    if maior_sim > 0.5:
        return escolher_resposta(respostas[melhor])

    return None


def processar_conversa(texto, state):
    respostas = state.respostas

    # 1. match por similaridade
    resp = encontrar_resposta(texto, respostas)
    if resp:
        return resp

    # 2. match simples (contém)
    for pergunta, resposta in respostas.items():
        if pergunta in texto.lower():
            return escolher_resposta(resposta)

    # 3. fallback
    return None