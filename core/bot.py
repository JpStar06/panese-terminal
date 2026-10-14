"""Comandos principais do bot (color, help, modo, exit)."""

from core.ui import gerar_painel_ajuda
from decorators.aiko import aiko_responde
from decorators.commands import comando, registry
from services.emotions import MODOS

CORES = {
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[0m",
}


@comando("color", "muda a cor da resposta (ex: /color red)", "Altera a cor do texto da resposta")
@aiko_responde()
def color(args, ctx=None, state=None):
    cor = args.strip().lower()
    if cor in CORES:
        state.cor_atual = CORES[cor]
        return f"Cor alterada para {cor}!"
    return f"Cor inválida. Cores válidas: {', '.join(CORES)}."


@comando("modo", "muda a personalidade (normal, femboy, tsundere)", "Uso: /modo <normal|femboy|tsundere>")
@aiko_responde()
def modo(args, ctx=None, state=None):
    escolhido = args.strip().lower()
    if escolhido not in MODOS:
        return f"Modo inválido. Modos disponíveis: {', '.join(MODOS)}."
    state.definir_modo(escolhido)
    return f"Modo {escolhido} ativado!"


@comando("help", "mostra ajuda", "Exibe esta mensagem de ajuda")
@aiko_responde()
def help_command(args, ctx=None, state=None):
    alvo = args.strip().lstrip("/").lower()

    if not alvo:
        texto = "\n╔══════════════════════════╗\n║   COMANDOS DISPONÍVEIS   ║\n╚══════════════════════════╝\n"
        for nome, cmd in registry.commands.items():
            texto += f"/{nome} - {cmd['help']}\n"
        return texto

    if not registry.get_command(alvo):
        return "Comando não encontrado."
    return gerar_painel_ajuda(registry, alvo)


@comando("exit", "sair do programa", "Encerra a aplicação")
@aiko_responde()
def exit_command(args, ctx=None, state=None):
    state.rodando = False
    return "Até logo! Vou ficar esperando você voltar 💗"
