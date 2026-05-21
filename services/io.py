import time

def print_lento(texto, delay=0.02):
    for linha in str(texto).split("\n"):
        for char in linha:
            print(char, end="", flush=True)
            time.sleep(delay)
        print()