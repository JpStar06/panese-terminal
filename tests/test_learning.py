import pytest

from core.state import AikoState
from services import learning, storage


@pytest.fixture
def dados(tmp_path, monkeypatch):
    base = tmp_path / "aiko_dados.json"
    storage.save_json(base, {"respostas": {"Olá!": ["oi"], "Tudo bem?": "sim"}})
    monkeypatch.setattr(storage, "RESPOSTAS_BASE", base)
    monkeypatch.setattr(storage, "MEMORIA_DIR", tmp_path / "memoria")
    return base


def test_normalizar():
    assert learning.normalizar("  Olá,   MUNDO!! ") == "ola mundo"
    assert learning.normalizar("oiiii") == "oi"
    assert learning.normalizar("???") == ""


def test_carrega_base_normalizada(dados):
    respostas = learning.carregar_respostas()
    assert respostas == {"ola": ["oi"], "tudo bem": ["sim"]}


def test_ensinar_salva_so_na_memoria_do_usuario(dados):
    state = AikoState("ana")
    state.respostas = learning.carregar_respostas("ana")
    learning.ensinar("Qual meu filme favorito?", "Interestelar", state)

    assert state.respostas["qual meu filme favorito"] == ["Interestelar"]
    assert "qual meu filme favorito" in learning.carregar_respostas("ana")
    assert "qual meu filme favorito" not in learning.carregar_respostas("bia")
    assert "qual meu filme" not in dados.read_text(encoding="utf-8")


def test_ensinar_acumula_respostas(dados):
    state = AikoState("ana")
    learning.ensinar("teste", "um", state)
    learning.ensinar("Teste!", "dois", state)
    assert learning.carregar_respostas("ana")["teste"] == ["um", "dois"]


def test_ensinar_pergunta_vazia(dados):
    with pytest.raises(ValueError):
        learning.ensinar("???", "x", AikoState("ana"))
