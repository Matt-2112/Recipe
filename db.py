import sqlite3

conn = sqlite3.connect("recipes.db")

c = conn.cursor()

#c.execute("""CREATE TABLE users (
#            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
#            username TEXT NOT NULL UNIQUE,
#            hash TEXT NOT NULL
#            )""")


conn.commit()

conn.close()

