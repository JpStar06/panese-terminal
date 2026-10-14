"""Decorador que aplica emoção, cor e efeito de digitação à resposta de um comando."""

from functools import wraps

from services.io import print_lento


def aiko_responde():
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            state = kwargs.get("state")
            texto = func(*args, **kwargs)
            if texto is None:
                return None
            final = state.aplicar_emocao(texto) if state else texto
            cor = state.cor_atual if state else ""
            print(f"{cor}Panese:\033[0m ", end="")
            print_lento(final)
            return final
        return wrapper
    return decorator
