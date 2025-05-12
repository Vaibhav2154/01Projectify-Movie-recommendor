# pip install streamlit

import streamlit as st
import requests
import pickle

# Laod movie titles
movies_dict =  pickle.load(open("movie_data.pkl","rb"))
movies = list(movies_dict['title'])

#background image
background_image_url = "https://wallpapercave.com/wp/wp5242993.jpg"
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("{background_image_url}");
        background-attachment: fixed;
        background-size: cover;
        background-position: center;
        opacity: 0.9;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Projectify Movie Recommender")
st.write("Get movie recommnedations by selecting any of your loved movie")

selected_movie_name = st.selectbox("Choose your favourite movie", movies)

if st.button("Recommend 🎉"):
    with st.spinner("Fetching recommendations..."):
        try:
            response = requests.get(
                "http://localhost:8000/recommend/",
                params={"movie": selected_movie_name}
            )
            data = response.json()
            st.subheader(f"Because you liked **{selected_movie_name}**:")
            for movie in data["recommendations"]:
                st.markdown(f"**🎬 {movie['title']}**")
        except Exception as e:
            st.error("Error fetching recommendations. Make sure FastAPI is running.")
            
st.markdown("#### by Vaibhav", unsafe_allow_html=True)
        

