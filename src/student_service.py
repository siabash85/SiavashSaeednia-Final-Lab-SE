class StudentService:
    def __init__(self):
        self.students = [
            {
                "id": 1,
                "full_name": "Siyavash Saeednia",
                "email": "siyavash@student.example.com",
                "major": "Software Engineering"
            },
            {
                "id": 2,
                "full_name": "Nima Rahimi",
                "email": "nima@student.example.com",
                "major": "Computer Engineering"
            }
        ]

    def get_all_students(self):
        return self.students

    def add_student(self, full_name: str, email: str, major: str):
        new_id = max([student["id"] for student in self.students], default=0) + 1

        new_student = {
            "id": new_id,
            "full_name": full_name,
            "email": email,
            "major": major
        }

        self.students.append(new_student)
        return new_student

    def get_student_by_id(self, student_id: int):
        for student in self.students:
            if student["id"] == student_id:
                return student

        return None
