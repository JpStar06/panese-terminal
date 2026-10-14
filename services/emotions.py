"""Efeitos de emoção aplicados às respostas, conforme o modo ativo."""

import random

MODOS = ("normal", "femboy", "tsundere")

# emoção -> (prefixo, sufixo); None = troca de letras
_EFEITOS = {
    "femboy": {
        "feliz": ("", " UwU"),
        "envergonhado": ("", " >///<"),
        "carinhoso": ("", " :3"),
        "brincalhão": None,
    },
    "tsundere": {
        "irritado": ("Hmph! ", ""),
        "envergonhado": ("", " >///<"),
        "orgulhoso": ("Tch! ", ""),
        "confuso": ("", " ...?"),
    },
}


def aplicar_emocao(texto, modo):
    """Devolve (texto_final, emocao_escolhida)."""
    efeitos = _EFEITOS.get(modo)
    if not efeitos:
        return texto, "neutro"

    emocao = random.choice(list(efeitos))
    efeito = efeitos[emocao]
    if efeito is None:
        return texto.replace("r", "w").replace("l", "w"), emocao

    prefixo, sufixo = efeito
    return f"{prefixo}{texto}{sufixo}", emocao
