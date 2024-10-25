# buscar :streamlit emoji shortscode
import streamlit as st

# Valores Default
nome  = ''
preco = 0.01
estoque = 10

#Configurações da pagina
st.set_page_config(
    page_title='Cadastro de produtos',
    page_icon='-shopping_troley:',
    layout='wide'
)

st.title('Cadastrar :coffee:')
st.subheader('Formulario para cadastrar produtos')

# Cria o formularip
with st.form(key='form_produto'):
    nome = st.text_input('Nome do produto', max_chars=60, placeholder='Nome com descrição do produto', value=nome)
    preco = st.number_input('Preço do produto', min_value=0.00, step=0.01, value=preco)
    estoque = st.number_input('Quantidade em estoque', min_value=0, step=1, value=estoque)

    # True ou False
    enviou = st.form_submit_button(label='Cadastrar')

# quando o formulario é enviado
if enviou:
    st.toast('Produto cadastrado com sucesso!')
    st.write(f'**Nome:** {nome}')
    st.write(f'**Preço** R${preco}')
    st.write(f'**Quantidade em estoque:** {estoque}')