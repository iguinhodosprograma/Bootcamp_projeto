import os
from pathlib import Path

import requests
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS

from src.estoque.funcoes import (
    alerta_estoque_baixo,
    atualizar_quantidade,
    cadastrar_produto,
    remover_produto,
)
from src.storage.estoque_armazenamento import carregar_estoque, salvar_estoque

# Raiz do projeto (dois níveis acima de src/api/servidor.py)
ROOT_DIR = Path(__file__).resolve().parents[2]

# ── App ────────────────────────────────────────────────────────────────────────
app = Flask(__name__, static_folder=str(ROOT_DIR))
CORS(app)


# ── Frontend ───────────────────────────────────────────────────────────────────
@app.get("/")
def index():
    """Serve o HTML principal."""
    return send_from_directory(str(ROOT_DIR), "estoque.html")


# ── Estoque ────────────────────────────────────────────────────────────────────
@app.get("/api/estoque")
def get_estoque():
    """Retorna todo o estoque atual como JSON."""
    return jsonify(carregar_estoque())


@app.post("/api/estoque")
def post_cadastrar():
    """Cadastra um novo produto. Body JSON: {nome, quantidade, limite_minimo}"""
    dados = request.get_json()
    estoque = carregar_estoque()
    try:
        cadastrar_produto(
            dados["nome"].upper(),
            int(dados["quantidade"]),
            int(dados["limite_minimo"]),
            estoque,
        )
        salvar_estoque(estoque)
        return jsonify({"ok": True, "mensagem": "Produto cadastrado com sucesso."}), 201
    except (ValueError, KeyError) as e:
        return jsonify({"ok": False, "mensagem": str(e)}), 400


@app.patch("/api/estoque/<nome>")
def patch_atualizar(nome):
    """Atualiza quantidade. Body JSON: {valor, operacao}, operacao: AUMENTAR | DIMINUIR"""
    dados = request.get_json()
    estoque = carregar_estoque()
    try:
        atualizar_quantidade(
            nome.upper(),
            int(dados["valor"]),
            dados["operacao"].upper(),
            estoque,
        )
        salvar_estoque(estoque)
        return jsonify({"ok": True, "mensagem": "Quantidade atualizada."})
    except (ValueError, KeyError) as e:
        return jsonify({"ok": False, "mensagem": str(e)}), 400


@app.delete("/api/estoque/<nome>")
def delete_produto(nome):
    """Remove um produto pelo nome."""
    estoque = carregar_estoque()
    try:
        remover_produto(nome.upper(), estoque)
        salvar_estoque(estoque)
        return jsonify({"ok": True, "mensagem": "Produto removido."})
    except ValueError as e:
        return jsonify({"ok": False, "mensagem": str(e)}), 404


@app.get("/api/estoque/alertas")
def get_alertas():
    """Retorna produtos abaixo do limite mínimo."""
    estoque = carregar_estoque()
    return jsonify(alerta_estoque_baixo(estoque))


# ── Clima (proxy OpenWeather) ──────────────────────────────────────────────────
@app.get("/api/clima")
def get_clima():
    """
    Proxy para a API OpenWeather.
    A key NUNCA é exposta ao navegador — vem da variável de ambiente OPENWEATHER_KEY.
    Query param: ?cidade=Recife,BR
    """
    cidade = request.args.get("cidade", "").strip()
    if not cidade:
        return jsonify({"erro": "Parâmetro 'cidade' é obrigatório."}), 400

    # CORRETO: lê o NOME da variável de ambiente, não a key em si
    api_key = os.environ.get("OPENWEATHER_KEY")
    if not api_key:
        return jsonify({"erro": "OPENWEATHER_KEY não configurada no servidor."}), 500

    try:
        resp = requests.get(
            "https://api.openweathermap.org/data/2.5/weather",
            params={
                "q": cidade,
                "appid": api_key,
                "units": "metric",
                "lang": "pt_br",
            },
            timeout=8,
        )
        return jsonify(resp.json()), resp.status_code
    except requests.exceptions.Timeout:
        return jsonify({"erro": "OpenWeather não respondeu a tempo."}), 504
    except requests.exceptions.RequestException as e:
        return jsonify({"erro": str(e)}), 502


# ── Entry point ────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    app.run(host = "0.0.0.0", port=5000, debug=False)
