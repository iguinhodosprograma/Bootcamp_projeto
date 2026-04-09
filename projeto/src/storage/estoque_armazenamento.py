import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
CAMINHO_ESTOQUE = BASE_DIR / "data" / "estoque.json"


def carregar_estoque():
    if not CAMINHO_ESTOQUE.exists():
        return {}

    with open(CAMINHO_ESTOQUE, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def salvar_estoque(estoque):
    with open(CAMINHO_ESTOQUE, "w", encoding="utf-8") as arquivo:
        json.dump(estoque, arquivo, ensure_ascii=False, indent=4)