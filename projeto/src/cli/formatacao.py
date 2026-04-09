def print_produtos(produtos):
    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    print("\nPRODUTOS EM ESTOQUE")
    print("-" * 30)

    for produto in produtos:
        status = "BAIXO" if produto["abaixo_do_limite"] else "OK"

        print(f"Nome: {produto['nome']}")
        print(f"Quantidade: {produto['quantidade']}")
        print(f"Status: {status}")
        print("-" * 30)


def print_alerta_estoque_baixo(produtos):
    if not produtos:
        print("Nenhum produto baixo em estoque.")
        return

    print("\nPRODUTOS QUE PRECISAM DE REPOSIÇÃO")
    print("-" * 30)

    for produto in produtos:
        print(f"Nome: {produto['nome']}")
        print(f"Quantidade: {produto['quantidade']}")
        print("-" * 30)