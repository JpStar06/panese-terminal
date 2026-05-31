# state.py
# Módulo responsável por gerenciar o estado do chatbot, incluindo emoções, modos de resposta
# e a aplicação de efeitos de emoção nas respostas. Ele define a classe AikoState, que mantém o estado atual do chatbot,
# como a emoção ativa, os modos de resposta (femboy e tsundere) e a cor atual das respostas. A classe também inclui métodos 
# para atualizar o estado emocional, ativar ou desativar modos específicos e aplicar efeitos de emoção nas respostas geradas, 
# permitindo que o chatbot responda de forma mais expressiva e personalizada com base no estado atual. Este módulo é fundamental 
# para criar uma experiência de conversa mais envolvente e dinâmica, adaptando as respostas do chatbot ao contexto emocional da interação.

import random

class AikoState:
    # estado do chatbot, incluindo emoção, modos e cor atual
    def __init__(self):
        self.emocao = "neutro"
        self.modo_femboy = False
        self.modo_tsundere = False
        self.cor_atual = "\033[35m"
        self.programas = {}
        self.respostas = {}
        self.nome = "Panese"

    # métodos para atualizar o estado emocional e aplicar efeitos nas respostas
    def atualizar_emocao(self, nova_emocao):
        self.emocao = nova_emocao

    # métodos para ativar ou desativar modos específicos
    def ativar_modo_femboy(self):
        self.modo_femboy = True

    def desativar_modo_femboy(self):
        self.modo_femboy = False
        self.emocao = "neutro"

    def ativar_modo_tsundere(self):
        self.modo_tsundere = True

    def desativar_modo_tsundere(self):
        self.modo_tsundere = False
        self.emocao = "neutro"

    # método para aplicar efeitos de emoção nas respostas geradas
    def aplicar_emocao(self, texto):
        t = texto
        if self.modo_femboy:
            emotions = ["feliz", "envergonhado", "carinhoso", "brincalhão"]
            self.emocao = random.choice(emotions)
            if self.emocao == "feliz":
                t += " UwU"
                return t
            elif self.emocao == "envergonhado":
                t += " >///<"
                return t
            elif self.emocao == "carinhoso":
                t += " :3"
                return t
            elif self.emocao == "brincalhão":
                t = t.replace("r", "w").replace("l", "w")
        elif self.modo_tsundere:
            emotions = ["irritado", "envergonhado", "orgulhoso", "confuso"]
            self.emocao = random.choice(emotions)
            if self.emocao == "irritado":
                t = "Hmph! " + t
                return t
            elif self.emocao == "envergonhado":
                t += " >///<"
                return t
            elif self.emocao == "orgulhoso":
                t = "Tch! " + t
                return t
            elif self.emocao == "confuso":
                t += " ...?"
                return t
        return t