from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import pg

load_dotenv()

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/students")
def get_students():
    print("Fetching Students...")
    return pg.read('students')

@app.get("/students/{id}")
def get_student(id: str):
    print("Fetching Student "+id+"...")
    return pg.read('students', id)