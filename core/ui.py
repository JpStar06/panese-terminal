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