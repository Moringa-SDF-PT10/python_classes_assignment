class TechnicalMentor(Person):
    def_init_(self, name, age, gender, complexion, employee_id, mode_of_teaching):
        super()._init_(name, age, gender, complexion)
        self.employee_id = employee_id
        self.courses =  []
        self.mode_of_teaching = mode_of_teaching

    def assign_course(self, course):
        if course not in self.courses:
            self.courses.append(course)

    def display_info(self):
        print(f"Employee ID: {self.employee_id}, Mode of teaching: {self.mode_of_teaching}, Courses: {self.courses}")