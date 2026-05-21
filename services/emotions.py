import random

def aplicar_emocao(texto, state):
    t = texto

    if state.emocao == "feliz":
        t = f"✨ {t}"

    if state.modo_tsundere:
        t = "Hmph. " + t

    if state.modo_femboy:
        t = "OwO " + t + " 💗"

    return t