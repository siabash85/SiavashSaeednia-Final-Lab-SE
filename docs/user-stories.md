# User Stories - University Registration System

## User Story 1: Course Registration with Prerequisite Validation

As a student,
I want to register for a course only if I have passed its prerequisite courses,
so that I can avoid registering for courses that I am not academically ready for.

### INVEST Check

| INVEST Criteria | Evaluation                                                                                         |
| --------------- | -------------------------------------------------------------------------------------------------- |
| Independent     | This story can be implemented independently from payment, grading, or transcript features.         |
| Negotiable      | The prerequisite rules can be changed based on university policies.                                |
| Valuable        | It helps students choose valid courses and prevents registration mistakes.                         |
| Estimable       | The required validation steps are clear: check student, course, capacity, and prerequisite status. |
| Small           | It focuses only on registering one student in one course.                                          |
| Testable        | It can be tested with both successful registration and failed prerequisite scenarios.              |

### Acceptance Criteria - Success Scenario

Given the student exists and has passed all prerequisite courses,
And the selected course has available seats,
When the student submits a course registration request,
Then the system should register the student in the selected course successfully.

### Acceptance Criteria - Error Scenario

Given the student exists but has not passed the required prerequisite course,
When the student submits a course registration request,
Then the system should reject the registration request and display an appropriate error message.

## User Story 2: View Available Courses by term

As a student,
I want to view available courses for a selected semester,
so that I can plan my course registration before the registration deadline.

### INVEST Check

| INVEST Criteria | Evaluation                                                                                           |
| --------------- | ---------------------------------------------------------------------------------------------------- |
| Independent     | This story can be developed separately from the actual course registration process.                  |
| Negotiable      | The course list can include different filters such as semester, department, professor, or capacity.  |
| Valuable        | It helps students make better decisions before registering for courses.                              |
| Estimable       | The required data is simple: course title, professor, semester, capacity, and available seats.       |
| Small           | It only focuses on displaying available courses, not registering the student.                        |
| Testable        | It can be tested by checking whether the system returns the correct courses for a selected semester. |

## User Story 3: Cancel Course Registration Before Deadline

As a student,
I want to cancel my registration from a course before the deadline,
so that I can update my semester schedule if my plan changes.

### INVEST Check

| INVEST Criteria | Evaluation                                                                                |
| --------------- | ----------------------------------------------------------------------------------------- |
| Independent     | This story can be implemented separately from adding a new course.                        |
| Negotiable      | The cancellation deadline and rules can be adjusted based on university regulations.      |
| Valuable        | It gives students flexibility to manage their semester schedule.                          |
| Estimable       | The logic is clear: check student, course registration, and deadline before cancellation. |
| Small           | It focuses only on cancelling one course registration.                                    |
| Testable        | It can be tested with valid cancellation and deadline-expired scenarios.                  |
