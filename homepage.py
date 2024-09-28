import streamlit as st

# containers
# columns

secao_usuario = st.session_state
nome_usuario = None

if "username" in secao_usuario:
    nome_usuario = secao_usuario.name

coluna_esquerda, coluna_direita = st.columns([1,1.5])

coluna_esquerda.title("Minha Empresa")
if nome_usuario:
    coluna_esquerda.write(f"#### Seja Bem Vindo, {nome_usuario}") #uso do Markdown

botao_dashboards = coluna_esquerda.button("Dashboards Projetos")
botao_indicadoires = coluna_esquerda.button("Principais Indicadores")

if botao_dashboards:
    st.switch_page("dashboard.py")
if botao_indicadoires:
    st.switch_page("indicadores.py")
    

container = coluna_direita.container(border=True)
container.image("imagens/bandeira.webp")