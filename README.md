# Estoque Loja de Açaí

![CI](https://github.com/Igor-C-Lima/Bootcamp_projeto/actions/workflows/ci.yml/badge.svg)

## 🌐 Aplicação publicada

**[https://seu-projeto.onrender.com](https://seu-projeto.onrender.com)**
*(substitua pelo link real após o deploy no Render)*

---

## Descrição do Problema

Pequenos quiosques de açaí, geralmente administrados por uma única pessoa,
enfrentam dificuldades para gerenciar o estoque de forma eficaz. Sem um
controle adequado, é difícil saber o que precisa ser reposto e o que entra
e sai da loja. Este projeto nasceu a partir de uma necessidade real: ajudar
uma conhecida, dona de um quiosque e que trabalha sozinha, a ter mais
controle sobre seu estoque de forma simples e prática.

## Proposta da Solução

Uma aplicação web com interface visual que permite cadastrar e remover
produtos, controlar quantidades e definir um limite mínimo de estoque
para cada item. É possível consultar quais produtos precisam de reposição
e, como diferencial, consultar o clima da cidade para antecipar a demanda
por açaí em dias de calor ou frio. O foco é na simplicidade, para que
qualquer pessoa consiga usar sem dificuldades técnicas.

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
- **Consultar o clima em tempo real** via integração com a API OpenWeather,
  com dica contextual sobre a demanda esperada por açaí

## Tecnologias Utilizadas

- Python 3.13
- Flask — servidor web e API REST
- Flask-CORS — suporte a requisições cross-origin
- Requests — consumo da API OpenWeather
- pytest — testes automatizados (unitários e de integração)
- ruff — análise estática e linting
- GitHub Actions — integração contínua (CI)
- Git — controle de versão
- Render — hospedagem em nuvem (deploy)

---

## Integração com API Externa

A aplicação consome a [API OpenWeather](https://openweathermap.org/api)
para exibir as condições climáticas de qualquer cidade. Com base na
temperatura retornada, o sistema sugere se é um bom momento para reforçar
o estoque (dias quentes) ou ser mais conservador na reposição (dias frios).

A chave da API fica armazenada exclusivamente no servidor — ela **nunca
é exposta ao navegador ou ao código-fonte**, garantindo segurança tanto
no ambiente local quanto no deploy em produção.

---

## Como Rodar Localmente

### Pré-requisitos

- Python 3.13+
- Uma chave de API gratuita do [OpenWeather](https://openweathermap.org/api)

### Instalação

```bash
# Clonar o repositório
git clone https://github.com/Igor-C-Lima/Bootcamp_projeto.git
cd Bootcamp_projeto/projeto

# Instalar dependências
pip install -r requirements.txt
```

### Configurar a chave da API

A key deve ser definida como variável de ambiente **antes** de subir o
servidor. Ela não deve ser colocada no código.

**Windows (PowerShell):**
```powershell
$env:OPENWEATHER_KEY="sua_chave_aqui"
```

**Windows (CMD):**
```cmd
set OPENWEATHER_KEY=sua_chave_aqui
```

**Mac/Linux:**
```bash
export OPENWEATHER_KEY="sua_chave_aqui"
```

### Subir o servidor

```bash
python -m src.api.servidor
```

Acesse em: **http://localhost:5000**

### Rodar a CLI (modo alternativo)

```bash
python run.py
```

### Testes

```bash
pytest tests/ -v
```

### Lint

```bash
ruff check .
```

---

## Estrutura do Projeto

```
projeto/
├── src/
│   ├── api/
│   │   └── servidor.py        # Servidor Flask + proxy OpenWeather
│   ├── cli/
│   │   └── cli.py             # Interface de linha de comando
│   ├── estoque/
│   │   └── funcoes.py         # Lógica de negócio do estoque
│   └── storage/
│       └── estoque_armazenamento.py  # Leitura e escrita do JSON
├── tests/
│   ├── test_estoque.py        # Testes unitários
│   └── test_integracao_clima.py  # Testes de integração (OpenWeather)
├── data/
│   └── estoque.json           # Dados persistidos
├── estoque.html               # Interface web
└── requirements.txt
```

---

## Informações

**Versão:** 2.0.0

**Autor:** Igor Christofidis de Lima — [github.com/Igor-C-Lima](https://github.com/Igor-C-Lima)

**Repositório:** [github.com/Igor-C-Lima/Bootcamp_projeto](https://github.com/Igor-C-Lima/Bootcamp_projeto)
