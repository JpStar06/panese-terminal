"""Entrada e saída do terminal: efeito de digitação e leitura com timeout."""

import os
import select
import sys
import time


def print_lento(texto, delay=0.02):
    """Imprime com efeito de digitação (sem atraso se a saída não for um terminal)."""
    if not sys.stdout.isatty():
        delay = 0
    for linha in str(texto).split("\n"):
        for char in linha:
            print(char, end="", flush=True)
            if delay:
                time.sleep(delay)
        print()


def _ler_bloqueante():
    linha = sys.stdin.readline()
    if linha == "":
        raise EOFError
    return linha.rstrip("\r\n")


def _ler_windows(timeout):
    import msvcrt

    limite = None if timeout is None else time.monotonic() + timeout
    buf = []
    while True:
        if msvcrt.kbhit():
            ch = msvcrt.getwch()
            if ch in ("\r", "\n"):
                print()
                return "".join(buf)
            if ch == "\x03":
                raise KeyboardInterrupt
            if ch == "\x1a":
                raise EOFError
            if ch == "\b":
                if buf:
                    buf.pop()
                    print("\b \b", end="", flush=True)
            elif ch in ("\x00", "\xe0"):
                msvcrt.getwch()  # tecla especial (setas etc.): ignora
            else:
                buf.append(ch)
                print(ch, end="", flush=True)
        else:
            if limite is not None and time.monotonic() >= limite:
                return None
            time.sleep(0.02)


def ler_linha(prompt="", timeout=None):
    """Lê uma linha do usuário.

    Devolve None se o tempo acabar e levanta EOFError se a entrada fechar
    (Ctrl+D / Ctrl+Z). Funciona em Linux, macOS e Windows.
    """
    print(prompt, end="", flush=True)
    if os.name == "nt":
        if sys.stdin.isatty():
            return _ler_windows(timeout)
        return _ler_bloqueante()  # sem terminal no Windows não há timeout
    if timeout is not None:
        pronto, _, _ = select.select([sys.stdin], [], [], timeout)
        if not pronto:
            return None
    return _ler_bloqueante()
