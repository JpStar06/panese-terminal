"""Estado da sessão: usuário, modo de personalidade, cor e respostas."""

from services.emotions import MODOS, aplicar_emocao


class AikoState:
    def __init__(self, usuario=None):
        self.usuario = usuario
        self.nome = "Panese"
        self.modo = "normal"
        self.emocao = "neutro"
        self.cor_atual = "\033[35m"
        self.respostas = {}
        self.rodando = True

    def definir_modo(self, modo):
        if modo not in MODOS:
            raise ValueError(f"Modo inválido: {modo}")
        self.modo = modo
        self.emocao = "neutro"

    def aplicar_emocao(self, texto):
        texto, self.emocao = aplicar_emocao(texto, self.modo)
        return texto
