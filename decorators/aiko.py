from services.io import print_lento
from services.emotions import aplicar_emocao
from core.state import AikoState
from functools import wraps

def aiko_responde(pensar=True):

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):

            state = kwargs.get("state")

            texto = func(*args, **kwargs)

            final = aplicar_emocao(texto, state)

            print(f"{state.cor_atual}Aiko:\033[0m ", end="")
            print_lento(final)

            return final

        return wrapper

    return decorator