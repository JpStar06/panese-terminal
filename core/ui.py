# ui.py
# Módulo responsável por gerar a interface de usuário do chatbot, incluindo banners animados,
# painéis de ajuda e a exibição dos comandos disponíveis. Ele utiliza caracteres ASCII para criar
# painéis estilizados e inclui funções para exibir informações de forma clara e organizada, facilitando
# a navegação e a compreensão dos usuários sobre as funcionalidades do chatbot. Este módulo é essencial
# para criar uma experiência de usuário mais agradável e intuitiva, permitindo que os usuários acessam
# facilmente as informações e comandos disponíveis, além de tornar a interação com o chatbot mais envolvente e personalizada.

from decorators.commands import registry
import time
import os

# Função para gerar um painel de comandos disponíveis, listando os comandos registrados no chatbot na inicialização
def gerar_painel_comandos(registry):
    linhas = []

    for nome, info in registry.commands.items():
        help_text = info.get("help", "")
        linhas.append(f"/{nome} - {help_text}")

    painel = "\n".join(linhas)

    return f"""
╔════════════════════════════════╗
║        PANESE ASSISTENTE       ║
╚════════════════════════════════╝

Comandos disponíveis:
{painel}

"""

# Função para gerar um painel de ajuda detalhado para um comando específico, exibindo o nome do comando e seus detalhes
def gerar_painel_ajuda(registry, nome):
    symbols = ["═", "║", "╔", "╗", "╚", "╝", " "]
    tamanho_nome = int(len(nome))
    painel_help = f"""\033[32m
{symbols[2]}{symbols[0]*3}{symbols[0]*tamanho_nome}{symbols[0]*3}{symbols[3]}
{symbols[1]}{symbols[6]*3}{nome}{symbols[6]*3}{symbols[1]}
{symbols[4]}{symbols[0]*3}{symbols[0]*tamanho_nome}{symbols[0]*3}{symbols[5]}
\033[0m
{{details}}
"""
    return painel_help.format(nome=nome, details=registry.get_command(nome).get("details", ""))


# Variáveis para os banners animados, contendo arte ASCII para exibição
BANNER = [
"""" 
██████╗  █████╗ ███╗   ██╗███████╗███████╗███████╗
██╔══██╗██╔══██╗████╗  ██║██╔════╝██╔════╝██╔════╝
██████╔╝███████║██╔██╗ ██║█████╗  ███████╗█████╗  
██╔═══╝ ██╔══██║██║╚██╗██║██╔══╝  ╚════██║██╔══╝
██║     ██║  ██║██║ ╚████║███████╗███████║███████╗
╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚══════╝╚══════╝
""",
]

BANNER_PRINCIPAL_LOGIN = ["""
╔══════════════════════╗
║      PANESE OS       ║
╠══════════════════════╣
║ [1] Login            ║
║ [2] Criar conta      ║
║ [3] Sair             ║
╚══════════════════════╝
"""]
BANNER_LOGIN = ["""
╔═════════════════════════════════════════════╗
║                 -=[LOGIN]=-                 ║
╠═════════════════════════════════════════════╣
║ Por favor, insira seu username e senha para ║
║ acessar o Panese Terminal.                  ║
╚═════════════════════════════════════════════╝
"""]

# Função para exibir um banner animado, imprimindo cada linha com um pequeno delay para criar um efeito visual agradável
def banner_animado(delay=0.01):
    print("\033[35m", end="")  # magenta
    for linha in BANNER:
        print(linha)
        time.sleep(delay)
    print("\033[0m", end="")

def banner_login_principal(delay=0.01):
    print("\033[35m", end="")  # magenta
    for linha in BANNER_PRINCIPAL_LOGIN:
        print(linha)
        time.sleep(delay)
    print("\033[0m", end="")

def banner_login(delay=0.01):
    print("\033[35m", end="")  # magenta
    for linha in BANNER_LOGIN:
        print(linha)
        time.sleep(delay)
    print("\033[0m", end="")