<h1 align="center">🎬 Online Movie Recommendation System</h1>

<p align="center">
  <b>A Python & SQL based Movie Recommendation Platform using Content-Based Filtering</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue"/>
  <img src="https://img.shields.io/badge/SQL-SQLite-lightgrey"/>
  <img src="https://img.shields.io/badge/Status-Completed-success"/>
</p>

---

## 📌 About the Project

The **Online Movie Recommendation System** is a beginner-friendly Python project that recommends movies to users based on their ratings and preferred genres.  
It demonstrates the fundamentals of **recommendation systems**, **database integration**, and **data processing** using Python and SQL.

This project is ideal for:
- Students learning Python & SQL
- Beginners exploring data-driven applications
- Resume and GitHub portfolio enhancement

---

## 🚀 Features

- ⭐ User-based movie ratings  
- 🎭 Genre-based recommendations  
- 🗄️ SQL database integration (SQLite)  
- 🧠 Content-based filtering logic  
- 📊 Data processing using Pandas  

---

## 🛠️ Tech Stack

| Category | Technologies |
|--------|-------------|
| Language | Python |
| Database | SQLite (SQL) |
| Libraries | Pandas |
| Tools | Git, GitHub |

---

## 🗃️ Database Design

**Movies Table**
- movie_id
- title
- genre
- release_year

**Users Table**
- user_id
- username

**Ratings Table**
- user_id
- movie_id
- rating

---

## ⚙️ How It Works

1. The system identifies movies rated **4 or higher** by the user  
2. Extracts genres from liked movies  
3. Recommends **unwatched movies** from the same genres  

This follows a **content-based recommendation approach**.

---

## ▶️ How to Run the Project

```bash
git clone https://github.com/USERNAME/movie-recommendation-system.git
cd movie-recommendation-system
pip install -r requirements.txt
python main.py
