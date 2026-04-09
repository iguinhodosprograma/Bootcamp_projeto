import pytest

@pytest.fixture
def estoque_testes():
    return {
        "açai": {
            "quantidade": 15,
            "limite_minimo": 5
        },
        "colher": {
            "quantidade": 50,
            "limite_minimo": 10
        }
    }