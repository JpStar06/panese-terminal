from core.bot import registry
from core.state import AikoState
from core.chat import processar_conversa
from services.learning import ensinar
from services.storage import load_json
from services.banner import banner_animado
from core.ui import gerar_painel_comandos
from services.io import print_lento

DATA_PATH = "data/aiko_dados.json"  # cor padrão


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
                from services.emotions import aplicar_emocao

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

if __name__ == "__main__":
    main()