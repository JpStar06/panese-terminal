from core.state import AikoState
from services.emotions import aplicar_emocao


def test_normal_nao_altera():
    assert aplicar_emocao("oi", "normal") == ("oi", "neutro")


def test_modos_alteram_o_texto():
    for modo in ("femboy", "tsundere"):
        for _ in range(30):
            texto, emocao = aplicar_emocao("olá, tudo bem?", modo)
            assert emocao != "neutro"
            assert texto != "olá, tudo bem?"


def test_state_troca_modo():
    state = AikoState("ana")
    state.definir_modo("tsundere")
    assert state.modo == "tsundere"
    state.definir_modo("normal")
    assert state.aplicar_emocao("oi") == "oi"
