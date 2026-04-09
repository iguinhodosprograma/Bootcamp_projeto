
def cadastrar_produto(nome_produto, quantidade, limite_minimo, estoque):
    if nome_produto.replace(" ", "") == "":
        raise ValueError("o nome nao pode ser vazio")
    if nome_produto in estoque:
        raise ValueError("o produto já existe")
    if quantidade < 0 or limite_minimo < 0:
        raise ValueError("nao sao permitidos valores negativos")
    
    estoque.update(
        {nome_produto: {"quantidade": quantidade, "limite_minimo": limite_minimo}}
    )


def listar_produtos(estoque):
    produtos_listados = []
    for nome_produto, dados in estoque.items():
        quantidade = dados["quantidade"]
        limite_minimo = dados["limite_minimo"]
        abaixo_do_limite = quantidade < limite_minimo
        
        produtos_listados.append({
            "nome": nome_produto,
            "quantidade": quantidade,
            "abaixo_do_limite": abaixo_do_limite
        })
    return produtos_listados


def atualizar_quantidade(nome_produto, valor, aumentar_diminuir, estoque):
    if nome_produto not in estoque:
        raise ValueError("o produto nao existe")
    if valor < 0:
        raise ValueError("o valor nao pode ser negativo")
    
    quantidade = estoque[nome_produto]["quantidade"]
    if aumentar_diminuir == "DIMINUIR": 
        quantidade -= valor
    elif aumentar_diminuir == "AUMENTAR": 
        quantidade += valor
        
    if quantidade < 0:
        raise ValueError("a quantidade final nao pode ser negativa")
    
    estoque[nome_produto]["quantidade"] = quantidade


def remover_produto(nome_produto, estoque):
    if nome_produto not in estoque:
        raise ValueError("o produto nao existe")
    
    estoque.pop(nome_produto)


def alerta_estoque_baixo(estoque):
    produtos_em_alerta = []
    for nome_produto, dados in estoque.items():
        quantidade = dados["quantidade"]
        limite_minimo = dados["limite_minimo"]

        if quantidade < limite_minimo:
            produtos_em_alerta.append({
                "nome": nome_produto,
                "quantidade": quantidade
            })

    return produtos_em_alerta


