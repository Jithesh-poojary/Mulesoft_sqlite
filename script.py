import sqlite3
connection = sqlite3.connect('fav_movies.db')
cursor = connection.cursor()
command1 = """CREATE TABLE IF NOT EXISTS 
movies(movie_id INTEGER PRIMARY KEY, movie_title TEXT, actor_name TEXT,
 year INTEGER, director_name TEXT)"""
cursor.execute(command1)
cursor.execute("INSERT INTO movies VALUES(1,'ABCD','Varun',2015,'Prabhudev')")
cursor.execute("INSERT INTO movies VALUES(2,'Charlie','Rakshith shetty',2022,'Kiran raj')")
cursor.execute("INSERT INTO movies VALUES(3,'gadar','sunny_deol',2001,'anil_sharma')")
cursor.execute("SELECT * FROM movies")
results = cursor.fetchall()
print(results)
print('Details of the movie in which Rakshith shetty was the lead actor')
cursor.execute("SELECT * FROM movies WHERE actor_name='Rakshith shetty'")
res = cursor.fetchall()
print(res)
