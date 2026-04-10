import os
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import RealDictCursor

load_dotenv()

def connect():
    return psycopg2.connect(
        dbname=os.environ.get('DBNAME'),
        user=os.environ.get('DBUSER'),
        password=os.environ.get('DBPASS'),
        host=os.environ.get('DBHOST')
    )

def create():
    pass

def read(table, id = None):
    query = f"SELECT * FROM ece.{table} "
    if id:
        query = query + "WHERE id = %s"
    conn = connect()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    if id:
        cur.execute(query, (id,))
        return cur.fetchone()
    else:
        cur.execute(query)
        return cur.fetchall()


def update():
    pass

def delete():
    pass

if __name__ == "__main__":
    print(read("users"))