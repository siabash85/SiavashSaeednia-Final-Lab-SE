from src.student_service import StudentService


def test_get_all_students_returns_list():
    # Arrange
    service = StudentService()

    # Act
    result = service.get_all_students()

    # Assert
    assert isinstance(result, list)
    assert len(result) >= 1


def test_add_student_successfully():
    # Arrange
    service = StudentService()

    # Act
    result = service.add_student(
        "Armin Kazemi",
        "armin@student.example.com",
        "Software Engineering"
    )

    # Assert
    assert result["id"] == 3
    assert result["full_name"] == "Armin Kazemi"
    assert result["email"] == "armin@student.example.com"
    assert result["major"] == "Software Engineering"


def test_get_student_by_id_not_found():
    # Arrange
    service = StudentService()
    invalid_student_id = 999

    # Act
    result = service.get_student_by_id(invalid_student_id)

    # Assert
    assert result is None
