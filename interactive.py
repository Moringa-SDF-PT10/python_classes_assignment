from person import Student

students = []
technical_mentors = []


def add_student():
    fields = [
        "name",
        "age",
        "gender",
        "complexion",
        "student_id",
        "courses",
        "mode_of_study",
    ]
    info = {}
    for field in fields:
        response = input(f"{field}?")
        if field == "age":
            info[field] = int(response)
        elif field == "courses":
            info[field] = [response]
        else:
            info[field] = response

    return Student(
        name=info["name"],
        age=info["age"],
        gender=info["gender"],
        complexion=info["complexion"],
        student_id=info["student_id"],
        courses=info["courses"],
        mode_of_study=info["mode_of_study"],
    )


if __name__ == "__main__":
    new_student = add_student()
    students.append(new_student)
    for student in students:

        print(student.display_info())
