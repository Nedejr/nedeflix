import streamlit as st
from login.service import login


def show_login():

    st.set_page_config(page_title= 'NedeFlix', page_icon=':cinema:', layout='centered')
    st.title('NEDEFLIX')
    username = st.text_input('Usuário')
    password = st.text_input('Senha', type='password')
    
    if st.button('Login'):
        login(
            username=username,
            password=password
            )
    
    