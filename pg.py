import os
from dotenv import load_dotenv
import psycopg2

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

def read():
    pass

def update():
    pass

def delete():
    pass