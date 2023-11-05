import sqlite3

def db_users_create():
  with sqlite3.connect('users.sqlite') as db:
      c = db.cursor()

  c.execute('''CREATE TABLE IF NOT EXISTS user (
            username TEXT NOT NULL PRIMARY KEY,
            password TEXT NOT NULL
              );''')

  db.commit()
  db.close()

def db_insert(username, password):
   with sqlite3.connect('users.sqlite') as db:
      c = db.cursor()

   c.execute('INSERT INTO user(username, password) VALUES (?, ?)', (username, password))
   db.commit()