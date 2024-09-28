# App_Streamlit

# Projeto Aplicativo Interno Empresarial com Streamlit

## Visão Geral
Este projeto é um aplicativo interno desenvolvido com o **Streamlit**, voltado para melhorar a eficiência e facilitar o acesso às informações da empresa. A aplicação possui diversos recursos para atender às necessidades dos colaboradores e gestores.

## Funcionalidades Principais

### 1. Imagens Carregadas
- O aplicativo permite o **upload e visualização de imagens** relevantes para o contexto empresarial.
- Essas imagens podem ser armazenadas e acessadas sempre que necessário, facilitando a comunicação visual de relatórios e atividades.

### 2. Multipáginas
- A aplicação é organizada em **múltiplas páginas**, cada uma dedicada a uma funcionalidade específica.
- Isso garante uma navegação intuitiva e facilita o acesso rápido a diferentes recursos do sistema.

### 3. Apresentações Gráficas e Indicadores
- O projeto conta com **gráficos e indicadores** para visualização de métricas empresariais.
- Utilizamos bibliotecas como **Matplotlib** e **Plotly** para gerar gráficos informativos que ajudam na tomada de decisão.

### 4. Sistema de Autenticação e Autorização
- Implementado um sistema de **autenticação** para garantir que apenas usuários autorizados possam acessar o aplicativo.
- Inclui recursos para **criar contas**, **login seguro** .
- **Autorização baseada em níveis de acesso**, permitindo diferenciar permissões para usuários e administradores.

### 5. Integração com Banco de Dados
- O aplicativo é integrado a um **banco de dados** para armazenamento e recuperação de informações de forma eficiente.
- Utiliza **SQLAlchemy** para comunicação com bancos de dados relacionais, permitindo um gerenciamento seguro e estruturado dos dados empresariais.

## Tecnologias Utilizadas
- **Streamlit**: Para construção da interface do usuário de maneira interativa e eficiente.
- **Python**: Linguagem principal utilizada no backend do projeto.
- **SQLAlchemy**: Biblioteca ORM para gerenciamento de bancos de dados.
- **Matplotlib/Plotly**: Para geração de gráficos e visualização de dados.
- **Bcrypt**: Para hashing de senhas e garantir a segurança dos dados de autenticação.

## Estrutura do Projeto
```plaintext
/
|-- PROJETO APP INTERNO EMPRESARIAL/
|   |-- images/
|   |-- database/
|   |-- .streamlit/
|   |-- __pycache__/
|   |-- criar_conta.py
|   |-- dashboard.py
|   |-- data_loader.py
|   |-- homepage.py
|   |-- indicadores.py
|   |-- dashboard.py
|   |-- main.py
|   |-- models.py

|-- README.md

