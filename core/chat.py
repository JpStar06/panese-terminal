"""Interpretação das mensagens e saída das respostas."""

import random
from difflib import SequenceMatcher

from services.io import ler_linha, print_lento
from services.learning import normalizar

LIMIAR_SIMILARIDADE = 0.8
TAMANHO_MINIMO_FUZZY = 5  # padrões/textos menores só casam exato ou por palavra inteira


def escolher_resposta(resp):
    if isinstance(resp, list):
        return random.choice(resp) if resp else None
    return resp


def encontrar_resposta(texto, respostas):
    """Procura a melhor resposta: exata > parecida > contém (palavra inteira)."""
    t = normalizar(texto)
    if not t:
        return None

    if t in respostas:
        return escolher_resposta(respostas[t])

    if len(t) >= TAMANHO_MINIMO_FUZZY:
        melhor, maior = None, 0.0
        for padrao in respostas:
            if len(padrao) < TAMANHO_MINIMO_FUZZY:
                continue
            sim = SequenceMatcher(None, t, padrao).ratio()
            if sim > maior:
                melhor, maior = padrao, sim
        if melhor is not None and maior >= LIMIAR_SIMILARIDADE:
            return escolher_resposta(respostas[melhor])

    candidatos = [p for p in respostas if f" {p} " in f" {t} "]
    if candidatos:
        return escolher_resposta(respostas[max(candidatos, key=len)])
    return None


def processar_conversa(texto, state):
    resposta = encontrar_resposta(texto, state.respostas)
    if resposta:
        return resposta.replace("{usuario}", state.usuario or "você")
    return None


def obter_input(timeout=10, state=None):
    """Lê a entrada. Devolve None se o tempo acabar; EOFError se a entrada fechar."""
    entrada = ler_linha("você: ", timeout=timeout)
    if entrada is not None:
        return entrada.strip()

    cor = state.cor_atual if state else ""
    print()
    print(f"{cor}Panese:\033[0m ", end="", flush=True)
    print_lento("Parece que você está ausente... Vou ficar aqui esperando 💗\n")
    return None


def responder(texto, state):
    """Aplica a emoção e imprime a resposta com efeito de digitação."""
    final = state.aplicar_emocao(texto)
    print(f"{state.cor_atual}Panese:\033[0m ", end="")
    print_lento(final)
