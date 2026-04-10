from fastapi import FastAPI
from dotenv import load_dotenv
import pg

load_dotenv()

app = FastAPI()

@app.get("/students")
def get_students():
    return pg.read('students')

@app.get("/students/{id}")
def get_student(id: str):
    return pg.read('students', id)