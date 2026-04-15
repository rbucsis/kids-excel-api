from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import pg
import models

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

@app.post("/students")
def post_student(req: models.PostStudent):
    student = req.model_dump()


    student['org_id'] = '67570c78-dcf1-40b3-860f-7539d98b4be8' ## FOR DEVELOPMENT ONLY DO NOT COMMIT TO GIT WITH THIS
    res = pg.create("students", student)
    print(res)
    return res

@app.put("/students/{id}")
def put_student(req):
    print(req)