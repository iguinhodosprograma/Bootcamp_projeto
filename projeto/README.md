# Estoque Loja de Açaí
![CI](https://github.com/iguinhodosprograma/Bootcamp_projeto/actions/workflows/ci.yml/badge.svg)

## Descrição do Problema

Pequenos quiosques de açaí, geralmente administrados por uma única pessoa,
enfrentam dificuldades para gerenciar o estoque de forma eficaz. Sem um
controle adequado, é difícil saber o que precisa ser reposto e o que entra
e sai da loja. Este projeto nasceu a partir de uma necessidade real: ajudar
uma conhecida, dona de um quiosque e que trabalha sozinha, a ter mais
controle sobre seu estoque de forma simples e prática.

## Proposta da Solução

Uma aplicação CLI simples e intuitiva que permite cadastrar e remover
produtos, controlar quantidades e definir um limite mínimo de estoque
para cada item. É possível consultar específicamente quais produtos precisam de reposição. 
O foco é na simplicidade, para que qualquer pessoa consiga usar sem dificuldades técnicas.

## Público-Alvo

Pequenos comerciantes que trabalham sozinhos ou com poucos funcionários
e enfrentam dificuldades para controlar seu estoque, muitas vezes
recorrendo a anotações em cadernos ou folhas avulsas. O sistema foi
pensado para ser simples o suficiente para qualquer pessoa usar, sem
necessidade de conhecimento técnico.

## Funcionalidades

- Cadastrar produtos no estoque
- Listar todos os produtos cadastrados
- Atualizar a quantidade de um produto
- Remover produtos do estoque
- Alertar quais produtos estão abaixo do limite mínimo e precisam de reposição

## Tecnologias Utilizadas

- Python 3.13
- pytest — testes automatizados
- ruff — análise estática e linting
- GitHub Actions — integração contínua
- Git — controle de versão

## Instalação

```bash
#Clonar repositório
git clone https://github.com/iguinhodosprograma/Bootcamp_projeto.git
cd Bootcamp_projeto/projeto

#Instalar dependências
pip install -r requirements.txt

#Execução (rodar o código no arquivo run.py)
python run.py

#Testes
pytest tests/ -v

#Lint
ruff check .

#Versão
1.0.0

#Autor
Igor Christofidis de Lima - github.com/iguinhodosprograma

#Repositório
github.com/iguinhodosprograma/Bootcamp_projeto
```

## Próximos Passos

Este projeto está em desenvolvimento contínuo. Após a entrega inicial,
estão planejadas as seguintes melhorias:

- Substituir a interface CLI por uma interface gráfica (GUI)
- Integrar um banco de dados para armazenamento mais robusto e consistente
- Implementar o sistema em um caso real em um quiosque de açaí