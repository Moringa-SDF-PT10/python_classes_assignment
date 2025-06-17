from main import Person

class TechnicalMentor (Person):
    def __init__(self, name, age, complexion, employee_id, mode_of_teaching, courses = [], gender = "Prefer not to say"):
        super().__init__(name, age, complexion, gender)
        self.employee_id = employee_id
        self.courses = courses
        self.mode_of_teaching = mode_of_teaching

    
    def assign_course(self, course):
        self.courses.append(course)

    def display_info(self):
        super().display_info()
        print(f"Employee ID: {self.employee_id}\nMode of Teaching: {self.mode_of_teaching}\nCourses: {self.courses}")

mode = TechnicalMentor("Mode", 73, "light", 328372, "Full-time")

mode.display_info()

mode.assign_course("Software Engineering")

print(mode.courses)