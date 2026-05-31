from decorators.commands import comando, registry
from decorators.aiko import aiko_responde
from datetime import datetime

@comando(name="horario", help_text="mostra horário atual", details="Exibe o horário atual")
@aiko_responde()
def horario(args, ctx=None, state=None):
    pegar_horario = datetime.now()
    agora = pegar_horario.strftime("%H:%M")
    return f"agora são {agora}"
