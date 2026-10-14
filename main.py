"""Ponto de entrada do Panese Terminal: login, carga da memória e loop de conversa."""

from core import bot  # noqa: F401  (registra os comandos principais)
import plugins  # noqa: F401  (registra os comandos dos plugins)
from core.chat import obter_input, processar_conversa, responder
from core.state import AikoState
from core.ui import gerar_painel_comandos
from decorators.commands import registry
from services import auth
from services.banner import banner_animado
from services.io import ler_linha, print_lento
from services.learning import carregar_respostas, ensinar


def tratar_comando(entrada, state):
    nome, _, args = entrada[1:].partition(" ")
    try:
        encontrado = registry.execute(nome.lower(), args.strip(), {"state": state})
    except Exception as erro:  # um comando com bug não derruba o programa
        print(f"Erro ao executar /{nome}: {erro}")
        return
    if not encontrado:
        print(f"Comando /{nome} não encontrado. Use /help.")


def tratar_conversa(entrada, state):
    resposta = processar_conversa(entrada, state)
    if resposta:
        responder(resposta, state)
        return

    cor = state.cor_atual
    print(f"{cor}Panese:\033[0m Não entendi...")
    if (ler_linha("Ensinar? (s/n): ") or "").strip().lower() != "s":
        return

    nova = (ler_linha("Resposta: ") or "").strip()
    if not nova:
        return
    try:
        ensinar(entrada, nova, state)
    except (ValueError, OSError) as erro:
        print(f"{cor}Panese:\033[0m Não consegui aprender isso ({erro})")
    else:
        print(f"{cor}Panese:\033[0m Aprendi isso 💗")


def conversar(usuario):
    state = AikoState(usuario)
    state.respostas = carregar_respostas(usuario)

    banner_animado(0.02)
    print_lento(gerar_painel_comandos(registry), 0.001)
    print(f"{state.cor_atual}Panese:\033[0m Oii {usuario}! Tô pronta pra conversar 💗")

    while state.rodando:
        try:
            entrada = obter_input(state=state, timeout=60)
            if not entrada:
                continue
            if entrada.startswith("/"):
                tratar_comando(entrada, state)
            else:
                tratar_conversa(entrada, state)
        except (EOFError, KeyboardInterrupt):
            print()
            print_lento(f"{state.cor_atual}Panese:\033[0m Até logo! 💗")
            break


def main():
    usuario = auth.autenticar()
    if usuario:
        conversar(usuario)


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print()
