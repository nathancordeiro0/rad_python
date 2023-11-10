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

def db_items_create():
    with sqlite3.connect('items.sqlite') as db:
        c = db.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS item (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        price INTEGER NOT NULL
        );''')

    db.commit()
    db.close()

# Database list CRUD
def db_insert(name, price):
    with sqlite3.connect('items.sqlite') as db:
        c = db.cursor()

    c.execute('INSERT INTO item VALUES (NULL,?,?)', (name, price))
    db.commit()
    db.close()

def db_view():
    with sqlite3.connect('items.sqlite') as db:
        c = db.cursor()

    c.execute('SELECT * FROM item')
    rows = c.fetchall()
    db.close()
    return rows

def db_delete(id):
    with sqlite3.connect('items.sqlite') as db:
        c = db.cursor()

    c.execute('DELETE FROM item WHERE id=?', (id,))
    db.commit()
    db.close()

def db_update(id, name, price):
    with sqlite3.connect('items.sqlite') as db:
        c = db.cursor()

    c.execute('UPDATE item SET name=?, price=? WHERE id=?', (name, price, id))
    db.commit()
    db.close()