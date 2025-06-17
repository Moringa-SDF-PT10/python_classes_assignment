from main import Person

class Student (Person):
    def __init__(self, name, age, complexion, student_id, mode_of_study, courses = [], gender="Prefer not to say"):
        super().__init__(name, age, complexion, gender)
        self.student_id = student_id
        self.courses = courses
        self.mode_of_study = mode_of_study
    
    def enrol(self, course):
        self.courses.append(course)

    def display_info(self):
        super().display_info()
        print(f"Student ID: {self.student_id}\nMode of Study: {self.mode_of_study}\nCourses: {[course for course in self.courses]}")

