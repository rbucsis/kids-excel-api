from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

@app.get("/students")
def get_students():
    return {"path": "students"}

@app.get("/students/{id}")
def get_student(id: str):
    return {"path": "students", "id": id}