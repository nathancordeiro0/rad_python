import sqlite3

conn = sqlite3.connect('users.sqlite')

cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users
               (id INTEGER PRIMARY KEY,
               name TEXT,
               password TEXT)''')

cursor.execute("INSERT INTO users (name, password) VALUES (?, ?)", ('admin', 'admin'))

conn.commit()
conn.close()
