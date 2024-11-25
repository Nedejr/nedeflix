import pandas as pd
import streamlit as st
from st_aggrid import AgGrid
from genres.service import GenreService
import json


def show_genres():
    genres_service = GenreService()
    genres = genres_service.get_genres()
    
    if genres:
        st.subheader('Lista de Gêneros')
        genres_df = pd.json_normalize(genres)
        AgGrid(
            data= pd.DataFrame(genres_df),
            #reload_data = True,
            key='genres_grid'
        )
    else:
        st.warning('Nenhum gênero cadastrado')

    st.divider()
    st.subheader('Cadastrar novo Gênero')
    name = st.text_input('Nome do Gênero')
    if st.button('Cadastrar'):
        new_genre = genres_service.create_genre(name_genre=name)
        if new_genre:
            st.rerun()
            st.success(f'Gênero {new_genre} cadastrado com sucesso.')
        else:
            st.error('Erro ao cadastrar o gênero')