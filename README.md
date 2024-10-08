# Dashboard de Reclamações em Python com Streamlit, Pandas, Numpy e Plotly

Este projeto cria um **dashboard interativo de reclamações** utilizando **Streamlit** como framework de deploy, integrando as bibliotecas **Pandas**, **Numpy** e **Plotly** para manipulação e visualização dos dados. O objetivo é apresentar uma análise interativa das reclamações, permitindo filtragens, agrupamentos e gráficos dinâmicos para uma melhor compreensão das tendências e categorias de reclamações.

## Introdução

O dashboard permite que os usuários visualizem reclamações de forma interativa. Ele oferece gráficos de distribuição, séries temporais, e permite o filtro por categorias, datas e severidade das reclamações. A interface é amigável e desenvolvida para facilitar a análise dos dados por qualquer usuário.

## Requisitos

- **Python 3.12**
- **Pandas**
- **Numpy**
- **Plotly**
- **Streamlit**

## Instalação

Para rodar este projeto localmente, siga os seguintes passos:

1. Clone o repositório:
    ```bash
    git clone https://github.com/usuario/projeto-dashboard-reclamacoes.git
    ```

2. Navegue até o diretório do projeto:
    ```bash
    cd projeto-dashboard-reclamacoes
    ```

3. Crie um ambiente virtual e ative-o:
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows use: venv\Scripts\activate
    ```

4. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

## Como Executar o Projeto

Para executar o dashboard localmente, basta rodar o comando abaixo:

```bash
streamlit run app.py
