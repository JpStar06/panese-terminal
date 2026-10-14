"""Banners em ASCII com animação linha a linha."""

import time

MAGENTA = "\033[35m"
RESET = "\033[0m"

BANNER = """██████╗  █████╗ ███╗   ██╗███████╗███████╗███████╗
██╔══██╗██╔══██╗████╗  ██║██╔════╝██╔════╝██╔════╝
██████╔╝███████║██╔██╗ ██║█████╗  ███████╗█████╗
██╔═══╝ ██╔══██║██║╚██╗██║██╔══╝  ╚════██║██╔══╝
██║     ██║  ██║██║ ╚████║███████╗███████║███████╗
╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚══════╝╚══════╝"""

BANNER_MENU_LOGIN = """╔══════════════════════╗
║      PANESE OS       ║
╠══════════════════════╣
║ [1] Login            ║
║ [2] Criar conta      ║
║ [3] Sair             ║
╚══════════════════════╝"""

BANNER_LOGIN = """╔═════════════════════════════════════════════╗
║                 -=[LOGIN]=-                 ║
╠═════════════════════════════════════════════╣
║ Por favor, insira seu username e senha para ║
║ acessar o Panese Terminal.                  ║
╚═════════════════════════════════════════════╝"""


def _animar(texto, delay):
    print(MAGENTA, end="")
    for linha in texto.split("\n"):
        print(linha)
        time.sleep(delay)
    print(RESET, end="")


def banner_animado(delay=0.02):
    _animar(BANNER, delay)


def banner_login_principal(delay=0.02):
    _animar(BANNER_MENU_LOGIN, delay)


def banner_login(delay=0.02):
    _animar(BANNER_LOGIN, delay)
