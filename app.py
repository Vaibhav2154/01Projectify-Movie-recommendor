from fastapi import FastAPI, HTTPException
#CORS 
# Cross origin resoure sharing
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import pickle

app = FastAPI()

app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

movies_dict = pickle.load(open("movie_data.pkl","rb"))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open("similarity.pkl","rb"))

@app.get('/')
def check():
  return { "message":"Working"}

@app.get('/recommend')
def recommend(movie: str):
  #check
  if movie not in movies['title'].values:
    raise HTTPException(status_code=404, detail="Movie is not found in the data")
  
  #load
  movie_index = movies[movies['title']== movie].index[0]
  distances = similarity[movie_index]
  movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
  print(movies_list)
  #process and return the value
  recommended_movies = [{
    "title": [movies.iloc[i[0]].title for i in movies_list]
  }]
  print(recommended_movies)
  return {"recommendations": recommended_movies}