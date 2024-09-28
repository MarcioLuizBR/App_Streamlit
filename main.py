import streamlit as st
import pandas as pd
import streamlit_authenticator as stauth
from models import session, Usuario

lista_usuario = session.query(Usuario).all()


credenciais = {"usernames":{usuario.email: {"name": usuario.nome, "password": usuario.senha} for usuario in lista_usuario}}

authenticator = stauth.Authenticate(credenciais, "credenciais_mlsp", "cv126dg6t5t8r1a23", cookie_expiry_days=30)

def autenticar_usuario(authenticator):
    nome, status_autenticacao, username = authenticator.login()
    
    if status_autenticacao:
        return {"nome": nome, "username": username}
    elif status_autenticacao == False:
        st.error("Combinação de usuario e senha inválidos")
    else:
        st.error("Preencha o formulário para fazer login")

def logout():
    authenticator.logout()


dados_usuario = autenticar_usuario(authenticator)

if dados_usuario:
    
    
    email_usuario = dados_usuario["username"]
    usuario = session.query(Usuario).filter_by(email=email_usuario).first()
    
    
    if usuario.admin:
        pg = st.navigation({
            "Home": [st.Page("homepage.py", title="HomeML" )],
            "Dashboards": [st.Page("dashboard.py", title="Dashboards"), st.Page("indicadores.py", title="Indicadores")],
            "Conta": [st.Page(logout, title="Sair"), st.Page("criar_conta.py", title="Criar Conta")],
        
        })
    else:
        pg = st.navigation({
        "Home": [st.Page("homepage.py", title="HomeML" )],
        "Dashboards": [st.Page("dashboard.py", title="Dashboards"), st.Page("indicadores.py", title="Indicadores")],
        "Conta": [st.Page(logout, title="Sair")]
        })
    
    pg.run()

