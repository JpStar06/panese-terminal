"""Memória de respostas: normalização de texto, carga e aprendizado."""

import re
import unicodedata

from services import storage


def normalizar(texto):
    """Minúsculas, sem acentos nem pontuação, sem letras repetidas em excesso."""
    texto = unicodedata.normalize("NFKD", str(texto))
    texto = "".join(c for c in texto if not unicodedata.combining(c)).lower()
    texto = re.sub(r"(.)\1{2,}", r"\1", texto)  # "oiii" -> "oi"
    texto = re.sub(r"[^a-z0-9]+", " ", texto)
    return texto.strip()


def _mesclar(destino, origem):
    for pergunta, respostas in origem.items():
        chave = normalizar(pergunta)
        if not chave:
            continue
        lista = respostas if isinstance(respostas, list) else [respostas]
        existentes = destino.setdefault(chave, [])
        existentes.extend(r for r in lista if r not in existentes)


def carregar_respostas(usuario=None):
    """Respostas base do projeto + o que este usuário ensinou."""
    respostas = {}
    _mesclar(respostas, storage.load_json(storage.RESPOSTAS_BASE).get("respostas", {}))
    if usuario:
        memoria = storage.load_json(storage.caminho_memoria(usuario))
        _mesclar(respostas, memoria.get("respostas", {}))
    return respostas


def ensinar(pergunta, resposta, state):
    """Memoriza uma resposta na sessão e no arquivo do usuário."""
    chave = normalizar(pergunta)
    if not chave:
        raise ValueError("A pergunta precisa ter letras ou números.")

    state.respostas.setdefault(chave, []).append(resposta)

    caminho = storage.caminho_memoria(state.usuario)
    memoria = storage.load_json(caminho)
    respostas = memoria.setdefault("respostas", {})
    atual = respostas.get(chave, [])
    if not isinstance(atual, list):
        atual = [atual]
    atual.append(resposta)
    respostas[chave] = atual
    storage.save_json(caminho, memoria)
