import sqlite3
db = itemGenerator.db


def create_connection(db):
    conn = None
    try:
        conn sqlite3.connect(db)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

