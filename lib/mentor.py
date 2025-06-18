from main import Person

class Mentor(Person):
    def __init__(self, name, age, gender, complexion, employee_id, mode_of_teaching):
        super().__init__(name, age, gender, complexion)
        self.employee_id = employee_id
        self.mode_of_teaching = mode_of_teaching
        self.courses = []
    
    def assign_course(self, course):
        self.courses.append(course)
        print(f"{self.name} has been assigned to teach {course}")
    
    def display_info(self):
        super().display_info()
        print(f"Mentor ID: {self.employee_id}")
        print(f"Mode of Teaching: {self.mode_of_teaching}")
        print("Mentor teaching:")
        for course in self.courses:
            print(f"- {course}")