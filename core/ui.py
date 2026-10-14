"""Painéis de comandos e de ajuda."""


def gerar_painel_comandos(registry):
    linhas = "\n".join(
        f"/{nome} - {info.get('help', '')}" for nome, info in registry.commands.items()
    )
    return f"""
╔════════════════════════════════╗
║        PANESE ASSISTENTE       ║
╚════════════════════════════════╝

Comandos disponíveis:
{linhas}

"""


def gerar_painel_ajuda(registry, nome):
    cmd = registry.get_command(nome)
    barra = "═" * (len(nome) + 6)
    return (
        f"\033[32m╔{barra}╗\n"
        f"║   {nome}   ║\n"
        f"╚{barra}╝\033[0m\n"
        f"{cmd.get('details', '')}\n"
    )
