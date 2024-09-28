import streamlit as st
from data_loader import carregar_dados
import plotly.express as px

base = carregar_dados()


def criar_card(icone, numero, texto, coluna_card):
    container = coluna_card.container(border=True)
    coluna_esquerda, coluna_direita = container.columns([1, 2.5])
    coluna_esquerda.image(f"imagens/{icone}")
    coluna_direita.write(numero)
    coluna_direita.write(texto)
    
coluna_esquerda, coluna_meio, coluna_direita = st.columns([1, 1, 1])

base_emandamento = base[base["Status"]=="Em andamento"]
base_fechado = base[base["Status"].isin({"Em andamento", "Finalizado"})]

criar_card("oportunidades.png", f'{base["Código Projeto"].count():,}' , "Oportunidade", coluna_esquerda)
criar_card("projetos_fechados.png", f'{base_fechado["Código Projeto"].count():,}' , "Projetos Fechados", coluna_meio)
criar_card("em_andamento.png", f'{base_emandamento["Código Projeto"].count():,}' , "Em andamento", coluna_direita)
criar_card("total_orcado.png",  f'R$ {base_fechado["Valor Orçado"].sum():,}', "Total Orçados", coluna_esquerda)
criar_card("total_pago.png", f'R$ {base_fechado["Valor Negociado"].sum():,}', "Total Pago", coluna_meio)
criar_card("desconto.png", f'R$ {base_fechado["Desconto Concedido"].sum():,}', "Total Desconto", coluna_direita)

base_status = base.groupby("Status", as_index=False).count()
base_status = base_status.rename(columns={"Código Projeto": "Quantidade"})
base_status = base_status.sort_values(by="Quantidade", ascending=False)


grafico = px.funnel(base_status, x="Quantidade", y="Status")
st.plotly_chart(grafico)