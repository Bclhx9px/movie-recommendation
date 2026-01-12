import sqlite3

conn = sqlite3.connect("movies.db")
cursor = conn.cursor()

movies = [
    (1, "Inception", "Sci-Fi", 2010),
    (2, "Interstellar", "Sci-Fi", 2014),
    (3, "Titanic", "Romance", 1997),
    (4, "The Notebook", "Romance", 2004),
    (5, "Avengers", "Action", 2012)
]

users = [
    (1, "Lahari"),
    (2, "User2")
]

ratings = [
    (1, 1, 5),
    (1, 3, 4),
    (2, 2, 5)
]

cursor.executemany("INSERT INTO movies VALUES (?, ?, ?, ?)", movies)
cursor.executemany("INSERT INTO users VALUES (?, ?)", users)
cursor.executemany("INSERT INTO ratings VALUES (?, ?, ?)", ratings)

conn.commit()
conn.close()

print("Sample data inserted")
