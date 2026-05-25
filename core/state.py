import random

class AikoState:
    def __init__(self):
        self.emocao = "neutro"
        self.modo_femboy = False
        self.modo_tsundere = False
        self.cor_atual = "\033[35m"
        self.programas = {}
        self.respostas = {}
    def atualizar_emocao(self, nova_emocao):
        self.emocao = nova_emocao
    def ativar_modo_femboy(self):
        emotions = ["feliz", "envergonhado", "carinhoso", "brincalhão"]
        self.emocaopr = random.choice(emotions)
        self.modo_femboy = self.emocaopr
    def desativar_modo_femboy(self):
        self.modo_femboy = False 