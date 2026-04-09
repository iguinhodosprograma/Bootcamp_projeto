from src.storage.estoque_armazenamento import carregar_estoque, salvar_estoque
from src.estoque.funcoes import (
    cadastrar_produto,
    listar_produtos,
    atualizar_quantidade,
    remover_produto,
    alerta_estoque_baixo
)
from src.cli.formatacao import print_produtos, print_alerta_estoque_baixo

estoque = carregar_estoque()

menu = """Selecione uma das opções seguintes:
1) Cadastrar produtos.
2) Listar produtos.
3) Atualizar a quantidade de um produto.
4) Produtos que precisam de reposição.
5) Remover produto do estoque.
6) Sair.

Sua escolha: """
bem_vindo = "Bem vindo ao seu gerenciador de estoque!"


print(bem_vindo)

def prompt_cadastrar_produto():
    nome_produto = input("Nome do produto: ").upper()
    quantidade = int(input("Quantidade já em estoque: "))
    limite_minimo = int(input("Quantidade mínima que deve ter em estoque: "))
    
    
    cadastrar_produto(nome_produto, quantidade, limite_minimo, estoque)
    salvar_estoque(estoque)
    print("\nProduto cadastrado com sucesso!\n")


def prompt_listar_produtos():
    produtos_listados = listar_produtos(estoque)
    print_produtos(produtos_listados)


def prompt_atualizar_quantidade():
    nome_produto = input("Nome do produto: ").upper()
    aumentar_diminuir = input(
        "Digite aumentar ou diminuir para alterar a quantidade como desejado:"
).upper()
    valor = int(input("Quantidade: "))
    
    
    atualizar_quantidade(nome_produto, valor, aumentar_diminuir, estoque)
    salvar_estoque(estoque)
    print("\nQuantidade atualizada com sucesso!\n")


def prompt_remover_produto():
    nome_produto = input("Nome do produto: ").upper()
    
    
    remover_produto(nome_produto, estoque)
    salvar_estoque(estoque)
    print("\nProduto removido com sucesso!\n")


def prompt_alerta_estoque_baixo():
    produtos_em_alerta = alerta_estoque_baixo(estoque)

    print_alerta_estoque_baixo(produtos_em_alerta)


def main():
    while (user_input := input(menu)) != "6":
        if user_input == "1":
            prompt_cadastrar_produto()
        elif user_input == "2":
            prompt_listar_produtos()
        elif user_input == "3":
            prompt_atualizar_quantidade()
        elif user_input == "4":
            prompt_alerta_estoque_baixo()
        elif user_input == "5":
            prompt_remover_produto()
        else:
            print("Escolha inválida, por favor tente novamente!")
            
    salvar_estoque(estoque)
    print("Saindo do sistema. Estoque salvo com sucesso!")
