# comandos/__init__.py
import importlib
import pkgutil

# Descobre e importa dinamicamente todos os módulos dentro desta pasta
for _, module_name, _ in pkgutil.walk_packages(__path__):
    importlib.import_module(f"{__name__}.{module_name}")