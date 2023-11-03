import sqlite3

conn = sqlite3.connect('users.sqlite')

cursor = conn.cursor()