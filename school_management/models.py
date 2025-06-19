class Person:
    def __init__(self, name, age, gender, complexion):
        self.name = name
        self.age = age
        self.gender = gender
        self.complexion = complexion
    
    def display_info(self):
        print(f"\nName: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Complexion: {self.complexion}")


class Student(Person):
    def __init__(self, name, age, gender, complexion, student_id, mode_of_study):
        super().__init__(name, age, gender, complexion)
        self.student_id = student_id
        self.mode_of_study = mode_of_study
        self.courses = []
    
    def enroll(self, course):
        if course not in self.courses:
            self.courses.append(course)
            return f"Enrolled in {course}"
        return f"Already enrolled in {course}"
    
    def display_info(self):
        super().display_info()
        print(f"Student ID: {self.student_id}")
        print(f"Mode of Study: {self.mode_of_study}")
        print("Courses:", ", ".join(self.courses) if self.courses else "None")


class TechnicalMentor(Person):
    def __init__(self, name, age, gender, complexion, employee_id, mode_of_teaching):
        super().__init__(name, age, gender, complexion)
        self.employee_id = employee_id
        self.mode_of_teaching = mode_of_teaching
        self.courses = []
    
    def assign_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
            return f"Assigned to teach {course}"
        return f"Already teaching {course}"
    
    def display_info(self):
        super().display_info()
        print(f"Employee ID: {self.employee_id}")
        print(f"Mode of Teaching: {self.mode_of_teaching}")
        print("Courses Teaching:", ", ".join(self.courses) if self.courses else "None")