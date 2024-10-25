import streamlit as st
import pandas as pd

# Cria um dicionario para simulação de dados
dados = {
    'Nome do produto' : ['Teclado', 'Mouse', 'Monitor', 'Processador'],
    'Desccrição' : ['Teclado Mecanico', 'MOuse sem fio', 'Monitor 24 pol.', 'Bem Rapidão'],
    'Preço' : [199.99, 99.00, 899.99, 1299.99],
    'Quntidade em estoque' : [10, 15, 10, 15]
}

# Converte dicionario em DataFrame
df1 = pd.DataFrame(dados)

# Exibir p DataFrame
st.subheader('DataFrame a partir do dicionario de dados')
st.dataframe(df1)

# Define URL do arquivo do Excel
url = 'https://softgraf.com/cursodatascience/produtos.xlsx'

# Le o arquivo da url e converte em DataFrame
df2 = pd.read_excel(url, engine='openpyxl')

# Exibe o DataFrame
st.subheader('DataFrame a partir do arquivo do Excel')
st.dataframe(df2)