import json

import pytest

from services import storage


def test_save_e_load(tmp_path):
    caminho = tmp_path / "a" / "dados.json"
    storage.save_json(caminho, {"x": "ç"})
    assert storage.load_json(caminho) == {"x": "ç"}
    assert not list(caminho.parent.glob("*.tmp"))


def test_arquivo_inexistente(tmp_path):
    assert storage.load_json(tmp_path / "nao.json") == {}


def test_corrompido_vira_backup_e_nao_e_sobrescrito(tmp_path):
    caminho = tmp_path / "dados.json"
    caminho.write_text("{quebrado", encoding="utf-8")
    assert storage.load_json(caminho) == {}
    assert not caminho.exists()
    backups = list(tmp_path.glob("dados.json.corrompido-*"))
    assert len(backups) == 1
    assert backups[0].read_text(encoding="utf-8") == "{quebrado"


@pytest.mark.parametrize("nome", ["../x", "a/b", "ab", "x" * 21, "com espaco", ""])
def test_username_invalido_nao_vira_caminho(nome):
    with pytest.raises(ValueError):
        storage.caminho_usuario(nome)
    with pytest.raises(ValueError):
        storage.caminho_memoria(nome)


def test_json_valido_gravado(tmp_path):
    storage.save_json(tmp_path / "a.json", {"a": 1})
    assert json.loads((tmp_path / "a.json").read_text(encoding="utf-8")) == {"a": 1}
