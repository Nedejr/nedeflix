import pandas as pd
import streamlit as st
from st_aggrid import AgGrid
from movies.service import MovieService
from datetime import datetime
from genres.service import GenreService
from actors.service import ActorService


def show_movies():
    movie_service = MovieService()
    movies = movie_service.get_movies()

    if movies:
        st.subheader('Lista de Filmes')
        movies_df = pd.json_normalize(movies)
        movies_df = movies_df.drop(columns=['actors','genre.id'])

        AgGrid(
            data= pd.DataFrame(movies_df),
            key='movies_grid'
        )
    else:
        st.warning('Nenhum filme cadastrado.')
    st.divider()
    st.subheader('Cadastrar Novo Filme')
    
    title = st.text_input('Titulo')

    release_date = st.date_input(label='Data de Lançamento',
                             value=datetime.today(),
                             min_value=datetime(1800, 1, 1).date(),
                             max_value=datetime.today(),
                             format='DD/MM/YYYY')
    
    genre_service = GenreService()
    genres = genre_service.get_genres()
    genre_names = {genre['name']:genre['id'] for genre in genres}

    select_genre_name = st.selectbox('Gênero', list(genre_names.keys()))
    
    actor_service = ActorService()
    actors = actor_service.get_actors()
    actor_names = {actor['name']:actor['id'] for actor in actors}

    select_actor_names = st.multiselect('Ator/Atriz', list(actor_names.keys()))
    select_actor_ids = [actor_names[name] for name in select_actor_names]

    resume = st.text_area('Resumo')

    if st.button('Cadastrar'):
        new_movie = movie_service.create_movie(
            title=title,
            release_date=release_date,
            genre=genre_names[select_genre_name],
            actors=select_actor_ids,
            resume=resume,
        )
        if new_movie:
            st.rerun()
        else:
            st.error('Erro ao cadastrar o filme na API.')

    