import pandas as pd
import streamlit as st
from st_aggrid import AgGrid
from reviews.service import ReviewService
from movies.service import MovieService

def show_reviews():

    review_service = ReviewService()
    reviews = review_service.get_reviews()

    if reviews:
        st.subheader('Lista de Avaliações')
        review_df = pd.json_normalize(reviews)
        AgGrid(
            data= pd.DataFrame(review_df),
            key='reviews_grid'
        )
    
    else:
        st.warning('Nenhuma avaliação encontrada.')
    st.divider()
    st.subheader('Cadastrar Nova Avaliação')

    movie_service = MovieService()
    movies = movie_service.get_movies()
    movie_titles = {movie['title']:movie['id'] for movie in movies}
    select_movie_title = st.selectbox('Filme', list(movie_titles.keys()))

    stars = st.number_input(
        label='Estrelas',
        min_value=1,
        max_value=5,
        step=1,)

    comment = st.text_area('Comentário')

    if st.button('Cadastrar'):
        new_review = review_service.create_review(
            movie=movie_titles[select_movie_title],
            stars=stars,
            comment=comment,
        )
        if new_review:
            st.rerun()
        else:
            st.error('Erro ao cadastrar a avaliação')



    

    