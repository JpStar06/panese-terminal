#import padrão do python
import sys

#imports de arquivos auxiliares
from decorators.commands import comando, registry
from decorators.aiko import aiko_responde
from datetime import datetime
from main import DATA_PATH
from core.state import AikoState
from core.ui import gerar_painel_ajuda

@comando("ping", "teste básico", "Responde com 'pong!' para verificar se o chatbot está funcionando")
@aiko_responde()
def ping(args, ctx=None, state=None):
    return "pong!"

@comando ("horario", "mostra horário atual", "Exibe o horário atual")
@aiko_responde()
def horario(args, ctx=None, state=None):
    pegar_horario = datetime.now()
    agora = pegar_horario.strftime("%H:%M")
    return f"agora são {agora}"

@comando("color", "muda a cor da resposta (ex: /color red)", "Altera a cor do texto da resposta")
@aiko_responde()
def color(args, ctx=None, state=None):
    cor = args.strip().lower()

    cores_validas = {
        "red": "\033[31m",
        "green": "\033[32m",
        "yellow": "\033[33m",
        "blue": "\033[34m",
        "magenta": "\033[35m",
        "cyan": "\033[36m",
        "reset": "\033[0m"
    }

    if cor in cores_validas:
        ctx["state"].cor_atual = cores_validas[cor]
        return f"Cor alterada para {cor}!"
    else:
        return "Cor inválida. Cores válidas: red, green, yellow, blue, magenta, cyan, reset."

@comando("help", "mostra ajuda", "Exibe esta mensagem de ajuda")
@aiko_responde()
def help_command(args, ctx=None, state=None):

    if not args:

        texto = """
╔══════════════════════════╗
║   COMANDOS DISPONÍVEIS   ║
╚══════════════════════════╝
"""

        for nome, cmd in registry.commands.items():
            texto += f"/{nome} - {cmd['help']}"

        return texto

    cmd = registry.get_command(args)

    if not cmd:
        return "Comando não encontrado."

    return gerar_painel_ajuda(registry, cmd['name'])

@comando("exit", "sair do programa", "Encerra a aplicação")
@aiko_responde()
def exit_command(args, ctx=None, state=None):
    sys.exit()
