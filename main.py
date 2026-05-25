#main.py
from core.bot import registry
from core.state import AikoState
from core.chat import processar_conversa
from services.learning import ensinar
from services.storage import load_json, save_json, save_usuarios
from services.banner import banner_animado
from core.ui import gerar_painel_comandos
from services.io import login
from services.io import print_lento
from services.emotions import aplicar_emocao
from services.data import DATA_PATH, DATA_USERS, carregar_dados

import os
class principal:
    def main():
        state = AikoState()

        # carregar memória
        dados = load_json(DATA_PATH)
        state.respostas = dados.get("respostas", {})

        # 🔥 Banner
        banner_animado(0.02)

        # 🔥 Painel
        painel = gerar_painel_comandos(registry)
        print_lento(painel, 0.001)

        print(f"{state.cor_atual}Panese:\033[0m Oii JpStar06! Tô pronta pra conversar 💗")

        while True:
            entrada = input("Você: ").strip()

            if not entrada:
                continue

            if entrada.startswith("/"):
                nome, *resto = entrada[1:].split(" ", 1)
                args = resto[0] if resto else ""

                ok = registry.execute(nome, args, {
                    "state": state
                })

                if not ok:
                    print("Comando não encontrado")

            else:
                resposta = processar_conversa(entrada, state)

                if resposta:

                    final = aplicar_emocao(resposta, state)

                    print(f"{state.cor_atual}Panese:\033[0m ", end="")
                    print_lento(final)

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
