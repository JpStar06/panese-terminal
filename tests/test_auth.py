import pytest

from services import auth, storage


@pytest.fixture(autouse=True)
def isolado(tmp_path, monkeypatch):
    monkeypatch.setattr(storage, "USERS_DIR", tmp_path / "users")
    monkeypatch.setattr(auth, "ITERACOES", 1000)  # rápido nos testes


def test_hash_e_verificacao():
    h = auth.hash_senha("segredo123")
    assert "segredo123" not in h
    assert auth.verificar_senha("segredo123", h)
    assert not auth.verificar_senha("errada", h)
    assert h != auth.hash_senha("segredo123")  # sal diferente


def test_verificar_senha_com_lixo():
    assert not auth.verificar_senha("x", "isso nao e um hash")
    assert not auth.verificar_senha("x", None)


def test_criar_e_logar():
    auth.criar_usuario("Ana_01", "senha123")
    assert auth.verificar_login("Ana_01", "senha123") == "Ana_01"
    assert auth.verificar_login("Ana_01", "outra") is None
    assert auth.verificar_login("naoexiste", "senha123") is None


def test_senha_nao_fica_em_texto_puro():
    auth.criar_usuario("ana", "senha123")
    assert "senha123" not in storage.caminho_usuario("ana").read_text(encoding="utf-8")


@pytest.mark.parametrize("nome", ["../hack", "a b", "ab", "x" * 21, ""])
def test_username_invalido(nome):
    with pytest.raises(ValueError):
        auth.criar_usuario(nome, "senha123")
    assert auth.verificar_login(nome, "senha123") is None


def test_senha_curta():
    with pytest.raises(ValueError):
        auth.criar_usuario("ana", "123")


def test_username_duplicado_ignora_maiusculas():
    auth.criar_usuario("Ana", "senha123")
    with pytest.raises(ValueError):
        auth.criar_usuario("ana", "senha123")


def test_migra_conta_antiga_em_texto_puro():
    storage.save_json(
        storage.caminho_usuario("antigo"), {"username": "antigo", "password": "1234"}
    )
    assert auth.verificar_login("antigo", "errada") is None
    assert auth.verificar_login("antigo", "1234") == "antigo"

    dados = storage.load_json(storage.caminho_usuario("antigo"))
    assert "password" not in dados and "senha_hash" in dados
    assert auth.verificar_login("antigo", "1234") == "antigo"
