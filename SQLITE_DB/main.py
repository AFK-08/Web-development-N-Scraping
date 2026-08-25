import sqlite3

database = sqlite3.connect("./SQLITE_DB/books_collection.db")

cursor = database.cursor()

cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")