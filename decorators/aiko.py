# aiko.py
# Decorador personalizado para as funções de comando do chatbot, responsável por aplicar efeitos de emoção nas
# respostas geradas. Ele utiliza a classe AikoState para acessar o estado atual do chatbot, como a emoção ativa
# e os modos de resposta, e aplica os efeitos correspondentes às respostas antes de exibi-las. Este decorador é
# essencial para criar uma experiência de conversa mais envolvente e personalizada, permitindo que o chatbot respononda
# de forma mais expressiva e adaptada ao contexto emocional da interação com os usuários.

from services.io import print_lento
from core.state import AikoState
from functools import wraps

# Decorador para aplicar os efeitos de emoção nas respostas do chatbot, utilizando o estado atual para determinar os efeitos a serem aplicados
def aiko_responde(pensar=True):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            state = kwargs.get("state")
            texto = func(*args, **kwargs)
            final = state.aplicar_emocao(texto)  # ✅
            print(f"{state.cor_atual}Panese:\033[0m ", end="")
            print_lento(final)
            return final
        return wrapper
    return decorator