import streamlit as st
# from ProjMain import recommend
import pickle
st.title("Movie Recommender System")
# st.text_input("Enter the movie name:")
movie_list= pickle.load(open('movie.pkl','rb'))
movies1 = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

movie_list = movies1['title'].values
option = st.selectbox("Choose a movie ",(movie_list))

def recommend(movie):
    movie_index = movies1[movies1['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies1.iloc[i[0]].title)
    return recommended_movies



# movie_list= movie_list['title'].values

if st.button("Recommend"):
    recommendations = recommend(option)
    for movie in recommendations:
        st.write(movie)
