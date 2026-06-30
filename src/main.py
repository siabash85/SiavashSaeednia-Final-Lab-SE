from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.student_service import StudentService


app = FastAPI(
    title="University Registration System API",
    description="A simple REST API for managing students in a university registration system.",
    version="1.0.0"
)

student_service = StudentService()


class StudentCreate(BaseModel):
    full_name: str
    email: str
    major: str


@app.get(
    "/api/students",
    tags=["Students"],
    summary="Get all students",
    description="Returns the list of all students stored in memory."
)
def get_students():
    return student_service.get_all_students()


@app.post(
    "/api/students",
    tags=["Students"],
    summary="Add a new student",
    description="Adds a new student to the in-memory students list."
)
def add_student(student: StudentCreate):
    return student_service.add_student(
        student.full_name,
        student.email,
        student.major
    )


@app.get(
    "/api/students/{student_id}",
    tags=["Students"],
    summary="Get student by ID",
    description="Returns one student based on the provided student ID."
)
def get_student(student_id: int):
    student = student_service.get_student_by_id(student_id)

    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    return student
