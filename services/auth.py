"""Contas de usuário: criação, hash de senha e login."""

import getpass
import hashlib
import hmac
import os
import time

from services import storage
from services.banner import banner_login, banner_login_principal
from services.io import print_lento

ITERACOES = 600_000
MIN_SENHA = 6


# ---------- senhas ----------

def hash_senha(senha, salt=None, iteracoes=None):
    salt = salt or os.urandom(16)
    iteracoes = iteracoes or ITERACOES
    dk = hashlib.pbkdf2_hmac("sha256", senha.encode("utf-8"), salt, iteracoes)
    return f"pbkdf2_sha256${iteracoes}${salt.hex()}${dk.hex()}"


def verificar_senha(senha, armazenado):
    try:
        algoritmo, iteracoes, salt, esperado = armazenado.split("$")
        if algoritmo != "pbkdf2_sha256":
            return False
        dk = hashlib.pbkdf2_hmac(
            "sha256", senha.encode("utf-8"), bytes.fromhex(salt), int(iteracoes)
        )
        return hmac.compare_digest(dk.hex(), esperado)
    except (ValueError, AttributeError):
        return False


# ---------- regras de conta (sem I/O de terminal, fáceis de testar) ----------

def criar_usuario(username, senha):
    """Cria a conta ou levanta ValueError com a mensagem para o usuário."""
    if not storage.USERNAME_RE.fullmatch(username):
        raise ValueError("Username inválido: use 3 a 20 letras, números ou _.")
    if len(senha) < MIN_SENHA:
        raise ValueError(f"A senha precisa ter pelo menos {MIN_SENHA} caracteres.")

    caminho = storage.caminho_usuario(username)
    existentes = (
        {p.stem.lower() for p in storage.USERS_DIR.glob("*.json")}
        if storage.USERS_DIR.exists()
        else set()
    )
    if username.lower() in existentes:
        raise ValueError("Username já existe.")

    storage.save_json(caminho, {"username": username, "senha_hash": hash_senha(senha)})
    return username


def verificar_login(username, senha):
    """Devolve o username se as credenciais estiverem certas, senão None.

    Contas antigas (senha em texto puro) são migradas para hash no primeiro
    login bem-sucedido.
    """
    if not storage.USERNAME_RE.fullmatch(username):
        return None

    caminho = storage.caminho_usuario(username)
    dados = storage.load_json(caminho)
    if not dados:
        return None

    nome = dados.get("username", username)

    if "senha_hash" in dados:
        return nome if verificar_senha(senha, dados["senha_hash"]) else None

    legado = dados.get("password")
    if isinstance(legado, str) and hmac.compare_digest(
        legado.encode("utf-8"), senha.encode("utf-8")
    ):
        dados.pop("password")
        dados["senha_hash"] = hash_senha(senha)
        storage.save_json(caminho, dados)
        return nome
    return None


# ---------- fluxo interativo ----------

def _fluxo_login():
    banner_login(0.03)
    username = input("Username: ").strip()
    senha = getpass.getpass("Password: ")
    usuario = verificar_login(username, senha)
    if usuario:
        print_lento(f"Bem-vindo {usuario}! 💗")
        return usuario
    time.sleep(1)  # atrasa tentativas em sequência
    print_lento("Usuário ou senha incorretos.")
    return None


def _fluxo_criar():
    username = input("Escolha um username: ").strip()
    senha = getpass.getpass("Escolha uma senha: ")
    if senha != getpass.getpass("Repita a senha: "):
        print_lento("As senhas não conferem.")
        return None
    try:
        usuario = criar_usuario(username, senha)
    except ValueError as erro:
        print_lento(str(erro))
        return None
    print_lento("Conta criada com sucesso 💗")
    return usuario


def autenticar():
    """Mostra o menu até o usuário entrar. Devolve o username ou None se sair."""
    while True:
        banner_login_principal(0.03)
        escolha = input("Escolha uma opção: ").strip()

        if escolha == "1":
            usuario = _fluxo_login()
        elif escolha == "2":
            usuario = _fluxo_criar()
        elif escolha == "3":
            print_lento("Saindo...")
            return None
        else:
            print_lento("Opção inválida.")
            continue

        if usuario:
            return usuario
