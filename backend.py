from sqlite3 import *


with connect('database.db') as db:
    cursor = db.cursor()
    query = """ CREATE TABLE IF NOT EXISTS table1(id INTEGER, name TEXT,  expenses TEXT )"""
    cursor.execute(query)

def information():
    cursor.execute("SELECT * FROM table1")
    return  cursor.fetchall()
