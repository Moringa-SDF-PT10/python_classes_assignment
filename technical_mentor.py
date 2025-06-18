import person
from person import Person

class TechnicalMentor(Person):
    def __init__(self, name,age, gender, complexion, employee_id,mode_of_teaching):
        super().__init__(name, age, gender, complexion)
        self.employee_id = employee_id
        self.mode_of_teaching= mode_of_teaching
        self.courses = []

    def assign_courses(self, course):
        if course not in self.courses:
            self.courses.append(course)

    def display_info(self):
        super().display_info()
        print(f"Employee ID: {self.employee_id}")
        print(f"courses: {self.courses}")
        print(f"Mode of teaching: {self.mode_of_teaching}")

Edgar = TechnicalMentor("Edgar","25", "Male", "Dark", "4423", "Hybrid")
Edgar.assign_courses("Software_Engineering")
Edgar.display_info()

