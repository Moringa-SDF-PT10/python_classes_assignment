class Student(Person):
    def_init_(self, name, age, gender, complexion, student_id, mode_of_study, courses):
        super()._init_(name, age, gender, complexion)
        self.student_id = student_id
        self.mode_of_study = mode_of_study
        self.courses = []
        
    def enroll(self, course):
        if course not in self.courses:
            self.courses.append(course)

    def display_info(self):
        print(f"Student ID: {self.student_id}, Mode of study: {self.mode_of_study}, Courses: {self.courses}")

    
        
        
