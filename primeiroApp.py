#.venv\scripts\activate.ps1]
# pip install streamlit

# stramlit run primeiroApp.py

import streamlit as st

# Titulo da pagina - url
st.title('Primeiro app :sunglasses:')
st.image('https://fly.metroimg.com/upload/q_85,w_700/https://uploads.metroimg.com/wp-content/uploads/2023/06/09094016/Neymar-Barcelona-5.jpg', width=500)

st.header('Este é um header com um divisor', divider='rainbow')
st.subheader('Este é um subheader: STreamlit é:blue[ legal]')
st.write('Este é um *Texto* comum')

"Texto Magico"
texto = 'Texto na Variavel'
texto

st.markdown('Markdown: *Streamlit* é **realmente** **legal**')
st.markdown('''
    :read[Streamlit] :orange[Streamlit] :orange[pode]
    :blue-blaclground[texto-destacado]
''')
st.text_input('None: ')

st.slider('Qual sua idade?', 0, 100, 25)

opcoes = st.multiselect('Selecione suas cores favoritas: ',
                        ['Verde', 'Amarelo', 'Azul', 'Rosa'],
                        ['Verde', 'Amarelo']
                        )

'Cores selecionadas'
st.write(opcoes)