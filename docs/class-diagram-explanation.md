# Class Diagram Relationship Explanation

## Professor and Course - Association

Professor and Course have an Association relationship because a professor teaches one or more courses, but both classes can exist independently. If a professor is removed from the system, the course information can still remain.

## Student and Enrollment - Composition

Student and Enrollment have a Composition relationship because an enrollment record belongs to a specific student. If the student is removed from the system, the related enrollment records should also be removed.

## Course and Enrollment - Aggregation

Course and Enrollment have an Aggregation relationship because a course can contain multiple enrollment records. However, the course can still exist even if there are no students enrolled in it.
