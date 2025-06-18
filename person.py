class Person:
    def __init__(self, name, age, gender, complexion):
        self.name = name
        self.age = age
        self.gender = gender
        self.complexion = complexion

    def display_info(self):
        info = f"name: {self.name} age: {self.age}"
        return info


class Student(Person):
    def __init__(
        self, name, age, gender, complexion, student_id, courses, mode_of_study
    ):
        super().__init__(name, age, gender, complexion)
        self.student_id = student_id
        self.courses = courses
        self.mode_of_study = mode_of_study

    def enroll(self, course):
        self.courses.append(course)

    def display_info(self):
        std_info = super().display_info()
        std_info += f" student_id: {self.student_id}"
        std_info += f" mode_of_study: {self.mode_of_study}"
        std_info += f" courses: {self.courses}"
        return std_info
    
    def dis(self):
        return Person.display_info(self)


class TechnicalMentor(Person):
    def __init__(
        self, name, age, gender, complexion, employee_id, mode_of_teaching, courses
    ):
        super().__init__(name, age, gender, complexion)
        self.employee_id = employee_id
        self.courses = courses
        self.mode_of_teaching = mode_of_teaching

    def assign_course(self, course):
        self.courses.append(course)

    def display_info(self):
        tm_info = super().display_info()
        tm_info += f" employee_id: {self.employee_id}"
        tm_info += f" mode_of_teaching: {self.mode_of_teaching}"
        tm_info += f" courses: {self.courses}"
        return tm_info


if __name__ == "__main__":
    student_s = Student(
        name="John",
        age=20,
        gender="M",
        complexion="dark",
        student_id="S003/2025",
        mode_of_study="part_time",
        courses=["JS, Python"],
    )
    tm_ian = TechnicalMentor(
        name="Ian",
        age=20,
        gender="M",
        complexion="dark",
        employee_id="S003/2025",
        mode_of_teaching="part_time",
        courses=["JS, Python"],
    )
    std_info = student_s.display_info()
    tm_info = tm_ian.display_info()
    print(std_info)
    print(tm_info)
    print(student_s.dis())
