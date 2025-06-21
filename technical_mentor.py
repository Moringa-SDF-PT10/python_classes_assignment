from school_system import Person

class TechnicalMentor(Person):
    def __init__(self, name, age, gender, complexion, employee_id, courses, mode_of_teaching):
        super().__init__(name, age, gender, complexion)
        self.employee_id = employee_id
        self.courses = courses
        self.mode_of_teaching = mode_of_teaching

    def assign_course(self, course):
        if course in self.courses:
            print(f"{course} already assigned")
        else:
            self.courses.append(course)
    
    def display_info(self):
        super().display_info()
        print(f"Employee ID: {self.employee_id}")
        print(f"Mode of Teaching: {self.mode_of_teaching}")
        print(f"Courses: {self.courses}")

charles = TechnicalMentor("Charles", 30, "male", "brown", "MTM-001", ["HTML", "CSS", "JavaScript"], "online")
# print(charles.display_info())
# print(charles.courses)