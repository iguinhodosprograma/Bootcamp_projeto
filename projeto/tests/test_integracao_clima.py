"""
Teste de integração — proxy /api/clima (OpenWeather)

Valida que o servidor consegue se comunicar com a API externa e
que o fluxo de dados não quebra a aplicação, usando mock para não
depender de rede ou de uma key real durante o CI.
"""

import pytest
from unittest.mock import MagicMock, patch

# Garante que a variável de ambiente existe antes de importar o servidor
import os
os.environ.setdefault("OPENWEATHER_KEY", "chave-de-teste-mock")

from src.api.servidor import app  # noqa: E402  (import após os.environ.setdefault)


# ── Fixture: cliente de teste Flask ───────────────────────────────────────────
@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as c:
        yield c


# ── Helpers ───────────────────────────────────────────────────────────────────
def _mock_openweather(cidade="Recife", temp=32.0, status=200):
    """Cria um mock da resposta requests.get simulando a OpenWeather."""
    mock = MagicMock()
    mock.status_code = status
    mock.json.return_value = {
        "name": cidade,
        "sys": {"country": "BR"},
        "weather": [{"description": "céu limpo"}],
        "main": {
            "temp": temp,
            "feels_like": temp - 2,
            "humidity": 75,
        },
        "wind": {"speed": 3.5},
    }
    return mock


# ── Testes ────────────────────────────────────────────────────────────────────
def test_clima_retorna_200_com_dados_validos(client):
    """Proxy deve retornar 200 e os dados da cidade quando a API responde ok."""
    with patch("requests.get", return_value=_mock_openweather("Recife", 32.0)):
        r = client.get("/api/clima?cidade=Recife")

    assert r.status_code == 200
    dados = r.get_json()
    assert dados["name"] == "Recife"
    assert dados["main"]["temp"] == 32.0


def test_clima_sem_parametro_cidade(client):
    """Deve retornar 400 quando o parâmetro 'cidade' não é informado."""
    r = client.get("/api/clima")
    assert r.status_code == 400
    assert "cidade" in r.get_json()["erro"].lower()


def test_clima_cidade_nao_encontrada(client):
    """Deve repassar o status 404 da OpenWeather quando a cidade não existe."""
    mock_404 = MagicMock()
    mock_404.status_code = 404
    mock_404.json.return_value = {"cod": "404", "message": "city not found"}

    with patch("requests.get", return_value=mock_404):
        r = client.get("/api/clima?cidade=CidadeInventada")

    assert r.status_code == 404


def test_clima_sem_api_key_configurada(client):
    """Deve retornar 500 quando OPENWEATHER_KEY não está no ambiente."""
    with patch.dict(os.environ, {}, clear=True):
        # Remove a key do ambiente para simular ausência
        os.environ.pop("OPENWEATHER_KEY", None)
        r = client.get("/api/clima?cidade=Recife")

    # Restaura para os próximos testes
    os.environ["OPENWEATHER_KEY"] = "chave-de-teste-mock"
    assert r.status_code == 500
    assert "OPENWEATHER_KEY" in r.get_json()["erro"]


def test_clima_timeout_openweather(client):
    """Deve retornar 504 quando a OpenWeather demora demais."""
    import requests as req_lib

    with patch("requests.get", side_effect=req_lib.exceptions.Timeout):
        r = client.get("/api/clima?cidade=Recife")

    assert r.status_code == 504