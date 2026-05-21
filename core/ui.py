from decorators.commands import registry

def gerar_painel_comandos(registry):
    linhas = []

    for nome, info in registry.commands.items():
        help_text = info.get("help", "")
        linhas.append(f"/{nome} - {help_text}")

    painel = "\n".join(linhas)

    return f"""
╔════════════════════════════════╗
║        PANESE ASSISTENTE       ║
╚════════════════════════════════╝

Comandos disponíveis:
{painel}

"""
def gerar_painel_ajuda(registry, nome):
    symbols = ["═", "║", "╔", "╗", "╚", "╝", " "]
    tamanho_nome = int(len(nome))
    painel_help = f"""\033[32m
{symbols[2]}{symbols[0]*3}{symbols[0]*tamanho_nome}{symbols[0]*3}{symbols[3]}
{symbols[1]}{symbols[6]*3}{nome}{symbols[6]*3}{symbols[1]}
{symbols[4]}{symbols[0]*3}{symbols[0]*tamanho_nome}{symbols[0]*3}{symbols[5]}
\033[0m
{{details}}
"""
    return painel_help.format(nome=nome, details=registry.get_command(nome).get("details", ""))