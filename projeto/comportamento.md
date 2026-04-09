1 cadastro de produtos
    usuário deve informar: 
        nome
        quantidade 
        limite mínimo do produto
    o sistema deve: 
        validar se o nome não está vazio
        validar se o nome do produto não existe
        validar se a quantidade inicial >= 0
        armazenar o produto
    caso algo esteja errado:
        impedir o cadastro
        informar erro

2 listagem de produtos
    usuário solicita
    o sistema deve:
        exibir produtos cadastrados
        mostrar nome e quantidade atual
        indicar caso o produto esteja abaixo do limite mínimo

3 atualizar quantidade
    usuário escolhe
        aumentar quantidade
        diminuir quantidade
    sistema deve:
        validar se o produto existe
        impedir que a quantidade final seja negativa
        atualizar o estoque corretamente

4 remoção de produto
    usuário solicita
    sistema deve:
        verificar se o produto existe
        remover do estoque
    se nao existir:
        informar erro

5 alerta de estoque baixo
    usuário solicita
    sistema deve:
        listar apenas produtos com quantidade menor que o limite mínimo
        informar nome e quantidade atual
