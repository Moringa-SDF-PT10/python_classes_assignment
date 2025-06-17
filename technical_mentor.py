from school_system import Person

class TechnicalMentor(Person):
    def __init__(self, employee_id, courses, mode_of_teaching):
        self.employee_id = employee_id
        self.courses = []
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
