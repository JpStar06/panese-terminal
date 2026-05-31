# io.py
# função de printar texto com efeito de digitação, criando uma experiência mais envolvente para o usuário. Ele também inclui um sistema de login simples, 
# permitindo que os usuários criem contas e façam login para acessar o chatbot. O módulo utiliza arquivos JSON para armazenar as informações dos usuários, 
# garantindo que os dados sejam persistentes entre as sessões. Além disso, ele inclui banners animados para tornar a interface mais atraente e acolhedora, 
# melhorando a experiência geral do usuário ao interagir com o chatbot.

import os
import time

from core.state import AikoState
from core.memory import (load_json, save_usuario, get_user_path)
from core.ui import (banner_login, banner_login_principal)

# Este módulo é responsável por lidar com as operações de entrada e saída do chatbot, incluindo a exibição de mensagens com efeitos visuais, o gerenciamento de login e criação de contas, e a manipulação de arquivos JSON para armazenar os dados dos usuários. Ele fornece funções para imprimir texto com um efeito de digitação, criar banners animados para a interface do usuário, e gerenciar o processo de autenticação dos usuários. Este módulo é essencial para criar uma experiência de usuário mais envolvente e personalizada, permitindo que os usuários se sintam mais conectados ao chatbot e tenham uma interação mais fluida e agradável.
def print_lento(texto, delay=0.02):
    for linha in str(texto).split("\n"):
        for char in linha:
            print(char, end="", flush=True)
            time.sleep(delay)
        print()


# Função para salvar os dados de um usuário, criando um arquivo JSON específico para cada usuário
class login:

    def principal_login():
        banner_login_principal(0.2)

        escolha = input("Escolha uma opção: ").strip()

        if escolha == "1":
            print_lento("Opção de Login selecionada 💗")
            return login.login()

        elif escolha == "2":
            print_lento("Criar conta selecionado 💗")
            return login.criar_conta()

        elif escolha == "3":
            print_lento("Saindo...")
            exit()

        else:
            print_lento("Opção inválida.")
            return False


    def login():
        banner_login(0.2)

        username = input("Username: ").strip()
        password = input("Password: ").strip()

        path = get_user_path(username)

        usuarios = load_json(path)

        if usuarios:

            if usuarios["password"] == password:
                print_lento(f"Bem-vindo {username}! 💗")
                return True

            else:
                print_lento("Senha incorreta.")
                return False

        else:
            print_lento("Usuário não encontrado.")
            return False


    def criar_conta():
        username = input("Escolha um username: ").strip()
        password = input("Escolha uma senha: ").strip()

        path = get_user_path(username)

        if os.path.exists(path):
            print_lento("Username já existe.")
            return False

        save_usuario({
            "username": username,
            "password": password
        })

        print_lento("Conta criada com sucesso 💗")

        time.sleep(1)

        return login.principal_login()
