from datetime import datetime

from decorators.aiko import aiko_responde
from decorators.commands import comando


@comando("horario", "mostra horário atual", "Exibe o horário atual")
@aiko_responde()
def horario(args, ctx=None, state=None):
    return f"agora são {datetime.now():%H:%M}"
