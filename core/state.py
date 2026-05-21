class AikoState:
    def __init__(self):
        self.emocao = "neutro"
        self.modo_femboy = False
        self.modo_tsundere = False
        self.cor_atual = "\033[35m"
        self.programas = {}
        self.respostas = {}