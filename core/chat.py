# chat.py
# Sistema de processamento de conversa, responsável por interpretar a entrada do usuário e gerar uma resposta adequada com base na memória do chatbot. 
# Ele utiliza técnicas de similaridade de texto para encontrar a melhor correspondência entre a pergunta do usuário e as perguntas armazenadas na 
# memória, permitindo que o chatbot responda de forma mais natural e relevante. Além disso, ele inclui funções para obter a entrada do usuário com 
# timeout e para imprimir a resposta com um efeito de digitação, tornando a interação mais fluida e envolvente.


import os
import sys
import time
import random
import select
from difflib import SequenceMatcher
from services.io import print_lento
from core.state import AikoState

ultimo_input = time.time()

# Função para escolher uma resposta aleatória se houver múltiplas opções
def escolher_resposta(resp):
    if isinstance(resp, list):
        return random.choice(resp)
    return resp

# Função para encontrar a resposta mais similar usando SequenceMatcher
def encontrar_resposta(pergunta, respostas):
    pergunta = pergunta.lower()
    melhor = None
    maior_sim = 0.0

    for padrao in respostas:
        sim = SequenceMatcher(None, pergunta, padrao).ratio()
        if sim > maior_sim:
            melhor = padrao
            maior_sim = sim

    if maior_sim > 0.6:  # aumentei um pouco o threshold
        return escolher_resposta(respostas[melhor])

    return None

# Função para processar a conversa, tentando encontrar a melhor resposta com base na similaridade e em fallback por contém
def processar_conversa(texto, state):
    respostas = state.respostas

    # 1. match por similaridade (mais preciso)
    resp = encontrar_resposta(texto, respostas)
    if resp:
        return resp

    # 2. fallback por contém (só se similaridade falhou)
    for pergunta, resposta in respostas.items():
        if pergunta in texto.lower():
            return escolher_resposta(resposta)

    # 3. fallback final
    return None

# Função para obter a entrada do usuário com timeout
def obter_input(timeout=10, state=None):
    print("você: ", end="", flush=True)
    # Aguarda a resposta do usuário
    pronto, _, _ = select.select([sys.stdin], [], [], timeout)
    if pronto:
        return sys.stdin.readline().strip()
    # Se der timeout, primeiro pulamos a linha do "você: "
    print() 
    # Agora imprimimos o nome e a mensagem na mesma linha, sem o \n no começo
    print(f"{state.cor_atual}Panese:\033[0m ", end="", flush=True)
    print_lento("Parece que você está ausente... Vou ficar aqui esperando 💗\n")

    return None

# Função para imprimir a resposta com efeito de digitação, aplicando emoçãos antes de imprimir
def obter_ouput(texto, state):  # renomeado de obter_ouput
    """Aplica emoção e imprime a resposta com efeito de digitação."""
    final = state.aplicar_emocao(texto)  # ✅ CORRIGIDO: usa state, não AikoState
    print(f"{state.cor_atual}Panese:\033[0m ", end="")
    print_lento(final)
