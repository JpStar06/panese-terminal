"""Leitura e escrita de arquivos JSON e caminhos de dados do projeto."""

import json
import os
import re
import tempfile
import time
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
USERS_DIR = DATA_DIR / "users"
MEMORIA_DIR = DATA_DIR / "memoria"
RESPOSTAS_BASE = DATA_DIR / "aiko_dados.json"

USERNAME_RE = re.compile(r"[A-Za-z0-9_]{3,20}")


def _nome_seguro(usuario):
    """Garante que o username não consegue escapar da pasta de dados."""
    if not isinstance(usuario, str) or not USERNAME_RE.fullmatch(usuario):
        raise ValueError("Username inválido: use 3 a 20 letras, números ou _.")
    return usuario


def caminho_usuario(usuario):
    return USERS_DIR / f"{_nome_seguro(usuario)}.json"


def caminho_memoria(usuario):
    return MEMORIA_DIR / f"{_nome_seguro(usuario)}.json"


def load_json(path, padrao=None):
    """Lê um JSON. Se o arquivo não existir, devolve o padrão (ou {}).

    Se o arquivo estiver corrompido, ele é movido para um backup
    (*.corrompido-<timestamp>) em vez de ser sobrescrito depois.
    """
    path = Path(path)
    vazio = {} if padrao is None else padrao
    if not path.exists():
        return vazio
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        backup = path.with_name(f"{path.name}.corrompido-{int(time.time())}")
        os.replace(path, backup)
        print(f"Aviso: {path.name} estava corrompido. Backup salvo em {backup.name}.")
        return vazio


def save_json(path, data):
    """Grava o JSON de forma atômica (arquivo temporário + os.replace)."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=path.parent, prefix=path.name + ".", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp, path)
    except BaseException:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise
