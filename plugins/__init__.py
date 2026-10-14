"""Descobre e importa todos os plugins desta pasta (cada um registra seus comandos)."""

import importlib
import pkgutil

for _, _nome, _ in pkgutil.iter_modules(__path__):
    try:
        importlib.import_module(f"{__name__}.{_nome}")
    except Exception as erro:  # um plugin quebrado não derruba o programa
        print(f"Aviso: plugin '{_nome}' não carregou: {erro}")
