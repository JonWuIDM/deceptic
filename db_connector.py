import psycopg2
from contextlib import contextmanager

def connect():
    return psycopg2.connect(database="blacklist", user="aakash", password="toor")

@contextmanager
def get_cursor():
    try:
        conn = connect()
        cursor = conn.cursor()
        yield cursor
    except:
        raise
    else:
        conn.commit()
    finally:
        cursor.close()
        conn.close()


def selectAll():
    with get_cursor() as cursor:
        cursor.execute("SELECT * FROM exploit_list;")
        return cursor.fetchall()

def insert(data):
    with get_cursor() as cursor:
        cursor.execute("INSERT INTO exploit_list(code) VALUES('%s')" % (data,))
