import sqlite3
import pandas as pd

conn = sqlite3.connect("movies.db")

movies = pd.read_sql("SELECT * FROM movies", conn)
ratings = pd.read_sql("SELECT * FROM ratings", conn)

def recommend_movies(user_id):
    user_ratings = ratings[ratings['user_id'] == user_id]
    liked = user_ratings[user_ratings['rating'] >= 4]

    liked_genres = movies[movies['movie_id'].isin(liked['movie_id'])]['genre']

    recommendations = movies[
        movies['genre'].isin(liked_genres) &
        ~movies['movie_id'].isin(liked['movie_id'])
    ]

    return recommendations[['title', 'genre']]

print("Recommended Movies:")
print(recommend_movies(1))

conn.close()
