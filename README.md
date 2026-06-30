# University Registration System - Final Lab SE

[![Python CI](https://github.com/siabash85/SiavashSaeednia-Final-Lab-SE/actions/workflows/ci.yml/badge.svg)](https://github.com/siabash85/SiavashSaeednia-Final-Lab-SE/actions/workflows/ci.yml)

## Student Information

Student Name: Siavash Saeednia
Student ID: 403880743

## Project Description

This project is a simple REST API for managing students in a university registration system.
It was developed as an individual final lab project for the Software Engineering course.

## Technologies Used

* Python
* FastAPI
* PyTest
* GitHub Actions
* Swagger / OpenAPI
* PlantUML

## Installation

```bash
git clone https://github.com/siabash85/SiavashSaeednia-Final-Lab-SE.git
cd SiavashSaeednia-Final-Lab-SE
python -m pip install -r requirements.txt
```

## Run the Application

```bash
python -m uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload
```

## Swagger UI

After running the application, open:

```text
http://127.0.0.1:8000/docs
```

In GitHub Codespaces, open the forwarded port 8000 and add:

```text
/docs
```

## API Endpoints

| Method | Endpoint                     | Description         |
| ------ | ---------------------------- | ------------------- |
| GET    | `/api/students`              | Get all students    |
| POST   | `/api/students`              | Add a new student   |
| GET    | `/api/students/{student_id}` | Get a student by ID |

## Run Unit Tests

```bash
python -m pytest -v
```

## Project Structure

```text
SiavashSaeednia-Final-Lab-SE/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── src/
│   ├── __init__.py
│   ├── main.py
│   └── student_service.py
│
├── tests/
│   └── test_student_service.py
│
├── docs/
│   ├── user-stories.md
│   ├── class-diagram.puml
│   ├── class-diagram.png
│   ├── class-diagram-explanation.md
│   ├── sequence-diagram.puml
│   └── sequence-diagram.png
│
└── .github/
    └── workflows/
        └── ci.yml
```

## Class Diagram Relationship Explanation

### Professor and Course - Association

Professor and Course have an Association relationship because a professor teaches one or more courses, but both classes can exist independently.

### Student and Enrollment - Composition

Student and Enrollment have a Composition relationship because an enrollment record belongs to a specific student. If the student is removed from the system, the related enrollment records should also be removed.

### Course and Enrollment - Aggregation

Course and Enrollment have an Aggregation relationship because a course can contain multiple enrollment records. However, the course can still exist even if there are no students enrolled in it.

## Final Checklist

* Public GitHub repository created
* Initial and final README completed
* Three user stories written using INVEST
* Acceptance criteria written using Given / When / Then
* Class diagram created using PlantUML
* Sequence diagram created using PlantUML
* REST API implemented using FastAPI
* Three unit tests written using PyTest
* GitHub Actions CI configured
* Swagger UI added and available
