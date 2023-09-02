import pickle
import streamlit as st
import pandas as pd
import requests

movies = pickle.load(open('./movie_list.pkl','rb'))
similarity = pickle.load(open('./similarity.pkl','rb'))
corrMatrix = pickle.load(open('./correlation_matrix.pkl', 'rb'))
movies_corr = pickle.load(open('./movie_data.pkl', 'rb'))
# print(type(similarity), similarity[:10])
# print(type(movies), movies[:10])


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters

def recommendusingsearch(q):
    # res = pd.DataFrame(columns=['movie_id', 'title', 'tags'])
    recommended_movie_names = []
    recommended_movie_posters = []
    for y,x,z in zip(movies.index, movies['tags'], movies['title']):
        if q.lower() in x.lower() or q.lower() in z.lower():
            match_list = movies.loc[y].values.flatten().tolist()
            recommended_movie_posters.append(fetch_poster(match_list[0]))
            recommended_movie_names.append(match_list[1])


    #         	res.loc[len(res.index)] = movies.loc[y].values.flatten().tolist()
    # return res
    return recommended_movie_names,recommended_movie_posters

def get_similar(movie_name,rating):
    similar_ratings = corrMatrix[movie_name]*(rating-2.5)
    similar_ratings = similar_ratings.sort_values(ascending=False)
    return similar_ratings

def recommendusingcorrelation(rate_tup):
    similar_movies = pd.DataFrame()
    for movie,rating in rate_tup:
        similar_movies = pd.concat([similar_movies, get_similar(movie,rating)],ignore_index = True, axis=1)
    m_list = similar_movies.sum(axis=1).sort_values(ascending=False).head(20).index
    m_ids = movies_corr[movies_corr['title'].isin(m_list)]['tmdbId'].values
    recommended_movie_names = list(movies_corr[movies_corr['title'].isin(m_list)]['title'].values)
    recommended_movie_posters = []
    for x in m_ids:
        recommended_movie_posters.append(fetch_poster(x))
    return recommended_movie_names, recommended_movie_posters


st.header('Movie Recommendation System')

# temp = '''
movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
# '''

query = st.text_input("Search Anything about a movie you want to find!")

if query:
    # st.dataframe(recommendusingsearch(query))
    names, posters = recommendusingsearch(query)
    if len(names) == 0:
        st.write("No movies matching the given query is present")
    else:
        # cols = st.columns(len(names))
        cnt = 0
        for x,y in zip(names, posters):
            if cnt % 5 == 0:
                cnt = 0
                cols = st.columns(5)
            with cols[cnt]:
                st.text(x)
                st.image(y)
            cnt += 1



movie_list_corr = movies_corr['title'].values
selected_movie_corr = st.multiselect(
        "Type or select a movie from the dropdown",
        movie_list_corr
        )

if st.button('Recommend'):
    selected_movie_corr = [(x, 5) for x in selected_movie_corr]
    names, posters = recommendusingcorrelation(selected_movie_corr)
    if len(names) == 0:
        st.write("No movies matching the given query is present")
    else:
        # cols = st.columns(len(names))
        cnt = 0
        for x,y in zip(names, posters):
            if cnt % 5 == 0:
                cnt = 0
                cols = st.columns(5)
            with cols[cnt]:
                st.text(x)
                st.image(y)
            cnt += 1


