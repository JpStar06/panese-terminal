#main.py
# Ponto de entrada principal para o chatbot, responsável por iniciar a aplicação, carregar os dados necessários e gerenciar o loop de conversa. 
# Ele utiliza a classe AikoState para manter o estado do chatbot durante a interação com os usuários, e integra os módulos de comandos, memória 
# e interface do usuário para criar uma experiência de conversa fluida e personalizada. Este arquivo é essencial para orquestrar as diferentes 
# partes do chatbot e garantir que ele funcione corretamente desde o início até o fim da interação com os usuários.

from decorators.commands import registry
from core.state import AikoState
from core import bot
from core.chat import processar_conversa, obter_input, obter_ouput
from core.memory import load_json, save_json, save_usuario, carregar_dados, carregar_usuario, ensinar, DATA_PATH, DATA_USERS_DIR, DATA_USERNAME
from core.ui import gerar_painel_comandos, banner_animado
from services.io import login
from services.io import print_lento

import plugins
import threading
import os

class principal:
    def main():
        #|_____________________________________|
        #|preparação antes de iniciar o chatbot|
        #|-------------------------------------|
        state = AikoState()

        # carregar memória
        dados = load_json(DATA_PATH)
        usuario = login.usuario
        state.respostas = dados.get("respostas", {})

        # 🔥 Banner
        banner_animado(0.02)

        # 🔥 Painel
        painel = gerar_painel_comandos(registry)
        print_lento(painel, 0.001)

        print(f"{state.cor_atual}Panese:\033[0m Oii {usuario}! Tô pronta pra conversar 💗")

        #iniciar loop de conversa
        while True:
            entrada = obter_input(state=state, timeout=60)

            if not entrada:
                continue
            #verificar se é comando
            if entrada.startswith("/"):
                nome, *resto = entrada[1:].split(" ", 1)
                args = resto[0] if resto else ""

                ok = registry.execute(nome, args, {
                    "state": state
                })

                if not ok:
                    print("Comando não encontrado")
            #se não for comando, processar conversa normal. fturamente colocar separado do loop principal para melhorar organização do código
            else:
                resposta = processar_conversa(entrada, state)

                if resposta:

                    obter_ouput(resposta, state)

                else:
                    print(f"{state.cor_atual}Panese:\033[0m Não entendi...")

                    aprender = input("Ensinar? (s/n): ").lower()

                    if aprender == "s":
                        nova = input("Resposta: ").strip()

                        if nova:
                            ensinar(entrada, nova, state, DATA_PATH)
                            print(f"{state.cor_atual}Panese: \033[0mAprendi isso 💗")

class carregar:
    def main():
        carregar_dados()
        autorizar = login.principal_login()
        if autorizar:
            principal.main()
        else:
            print_lento("Falha na autenticação. voltando para o menu principal de login.")
            carregar.main()
if __name__ == "__main__":
    carregar.main()
