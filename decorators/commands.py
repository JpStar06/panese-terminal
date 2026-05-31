# commands.py
# Módulo responsável por gerenciar os comandos do chatbot, permitindo o registro e a execução
# de comandos personalizados. Ele define a classe CommandRegistry, que mantém um registro dos comandos disponíveis,
# incluindo suas funções associadas, descrições de ajuda e detalhes. O decorador @comando é utilizado para registrar
# facilmente novas funções de comando, facilitando a expansão das funcionalidades do chatbot. Este módulo é
# essencial para criar uma experiência de conversa mais interativa e personalizada, permitindo que os usuários
# acessem uma variedade de comandos para interagir com o chatbot de maneiras diferentes, além de fornecer informações
# claras sobre o uso de cada comando.

class CommandRegistry:
    # classe para registrar e gerenciar os comandos do chatbot, armazenando as funções associadas, descrições de ajuda e detalhes
    def __init__(self):
        self.commands = {}

    # método para registrar um comando, associando um nome, função, descrição de ajuda e detalhes
    def register(self, name, func, help_text="", details=""):
        self.commands[name] = {
            "name": name,
            "func": func,
            "help": help_text,
            "details": details
            }

    # método para executar um comando, verificando se o comando existe e chamando a função associada com os argumentos e contexto fornecidos
    def execute(self, name, args, ctx):
        cmd = self.commands.get(name)

        if not cmd:
            return False

        cmd["func"](args, ctx=ctx, state=ctx.get("state"))

        return True

    # método para obter as informações de um comando específico, retornando um dicionário com os detalhes do comando registrado
    def get_command(self, name):
        return self.commands.get(name)

registry = CommandRegistry()

# decorador para registrar uma função como um comando do chatbot, associando um nome, descrição de ajuda e detalhes para facilitar o registro de novos comandos
def comando(name, help_text="", details=""):
    def decorator(func):

        registry.register(name, func, help_text, details)

        return func
    return decorator