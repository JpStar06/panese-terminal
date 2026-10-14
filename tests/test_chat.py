from core.chat import encontrar_resposta, processar_conversa
from core.state import AikoState
from services.learning import normalizar

BASE = {
    "oi": ["oii"],
    "ola": ["olá"],
    "bom dia": ["bom dia!"],
    "qual seu nome": ["Aiko"],
    "bom dia pessoal": ["bom dia, galera"],
}


def resp(texto):
    return encontrar_resposta(texto, {normalizar(k): v for k, v in BASE.items()})


def test_ignora_maiusculas_acentos_e_pontuacao():
    assert resp("OI!") == "oii"
    assert resp("Olá") == "olá"
    assert resp("Qual seu nome?") == "Aiko"


def test_letras_repetidas():
    assert resp("oiiii") == "oii"


def test_erro_de_digitacao():
    assert resp("bom diaa") == "bom dia!"


def test_texto_curto_ou_vazio_nao_casa():
    assert resp("o") is None
    assert resp("") is None
    assert resp("???") is None


def test_nao_casa_pedaco_de_palavra():
    assert resp("boi") is None
    assert resp("cola") is None


def test_contem_palavra_inteira_prefere_o_mais_especifico():
    assert resp("oi aiko, tudo bem") == "oii"
    assert resp("bom dia pessoal lindo") == "bom dia, galera"


def test_sem_resposta():
    assert resp("me conta uma piada") is None


def test_substitui_usuario():
    state = AikoState("Ana")
    state.respostas = {"ola": ["oii {usuario}!"]}
    assert processar_conversa("olá", state) == "oii Ana!"
