import sqlite3


def connect(query):
    with sqlite3.connect('animal.db') as con:
        cur = con.cursor()
        cur.execute(query)
        result = cur.fetchall()
    return result

