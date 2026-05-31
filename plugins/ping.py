from decorators.commands import comando, registry
from decorators.aiko import aiko_responde

@comando("ping", "teste básico", "Responde com 'pong!' para verificar se o chatbot está funcionando")
@aiko_responde()
def ping(args, ctx=None, state=None):
    return "pong!"
