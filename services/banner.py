import time

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
╔═══════════════════════════════════════════════════════════════╗
║                 Bem-vindo ao Panese Terminal!                 ║
║  Por favor, faça login ou crie uma nova conta para continuar. ║
╚═══════════════════════════════════════════════════════════════╝

1) Login
2) Criar nova conta
3) Sair
"""]
BANNER_LOGIN = ["""
╔════════════════════════════════════════════════════════════════════════╗
║                                  LOGIN                                 ║
║ Por favor, insira seu username e senha para acessar o Panese Terminal. ║
╚════════════════════════════════════════════════════════════════════════╝
"""]

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