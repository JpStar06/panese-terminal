#io.py
from .data import DATA_PATH, DATA_USERS
from services.storage import load_json, save_usuarios
from services.banner import banner_login, banner_login_principal
import time


def print_lento(texto, delay=0.02):
    for linha in str(texto).split("\n"):
        for char in linha:
            print(char, end="", flush=True)
            time.sleep(delay)
        print()

class login:
    def principal_login(autorizar=False):
        banner_login_principal(0.02)
        escolha = input("Escolha uma opção: ").strip()
        if escolha == "1":
            print_lento("Opção de Login selecionada. 💗")
            return login.login()
        elif escolha == "2":
            print_lento("Opção de Criar nova conta selecionada. 💗")
            login.criar_conta()
            return False
        elif escolha == "3":
            print_lento("Saindo... Até a próxima! 💗")
            time.sleep(1)
            exit()
        else:
            print_lento("Opção inválida. Por favor, tente novamente.")
            return False
    
    def login():
        banner_login(0.02)
        username = input("Username: ").strip()
        password = input("Password: ").strip()

        usuarios = load_json(DATA_USERS)

        if username in usuarios and usuarios[username]["password"] == password:
            print_lento(f"Login bem-sucedido! Bem-vindo, {username}! 💗")
            return True
        else:
            print_lento("Login falhou. Username ou senha incorretos. Por favor, tente novamente.")
            time.sleep(1)
            return False  # Volta para o menu principal de login

    def criar_conta():
        Username = input("Escolha um username: ").strip()
        Password = input("Escolha uma senha: ").strip()
        usuarios = load_json(DATA_USERS)
        if Username in usuarios:
            print_lento("Username já existe. Por favor, escolha outro.")
        else:
            usuarios[Username] = {"password": Password}
            save_usuarios(usuarios)
            print_lento("Conta criada com sucesso! Agora você pode fazer login. 💗")
            time.sleep(1)
            return login.principal_login()
        