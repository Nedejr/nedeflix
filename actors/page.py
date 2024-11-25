import pandas as pd
import streamlit as st
from st_aggrid import AgGrid
from actors.service import ActorService
from datetime import datetime


def show_actors():
    actor_service = ActorService()
    actors = actor_service.get_actors()
    st.subheader('Lista de Atores/Atrizes')
    
    if actors:
        actors_df = pd.json_normalize(actors)
        AgGrid(
            data= pd.DataFrame(actors_df),
            key='actors_grid'
        )
    else:
        st.warning('Nenhum ator/atriz cadastrado')
    st.divider()
    st.subheader('Cadastrar novo Ator/Atriz')
    name = st.text_input('Nome do ator/atriz')
    birthday = st.date_input(label='Data de Nascimento',
                             value=datetime.today(),
                             min_value=datetime(1800, 1, 1).date(),
                             max_value=datetime.today(),
                             format='DD/MM/YYYY')
    nationality_list = ['BRAZIL', 'USA']
    nationality = st.selectbox(
                    label='Nacionalidade',
                    options=nationality_list)
    
    if st.button('Cadastrar'):
        new_actor = actor_service.create_actor(name_actor=name, birthday_actor=birthday, nationality_actor=nationality)
        if new_actor:
            st.rerun()
            st.success(f'{name} cadastrado com sucesso')
        else:
            st.error('Erro ao cadastrar o Ator/Atriz.')