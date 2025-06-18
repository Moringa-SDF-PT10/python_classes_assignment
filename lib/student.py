from main import Person

class Student(Person):
    def __init__(self,name, age, gender, complexion,student_id,mode_of_study,courses):
        # Person.__init__(self, name, age, gender, complexion)
        super().__init__(name, age, gender, complexion)
        self.student_id = student_id
        self.mode_of_study = mode_of_study
        self.courses = []

    def enroll(self, course):
        self.courses.append(course)
        print(f"{self.name} has been enrolled in {course}")
    
    def display_info(self):
        super().display_info()
        print(f"Student ID: {self.student_id}")
        print(f"Study mode: {self.mode_of_study}")
        print("Courses enrolled:")
        for course in self.courses:
            print(f"- {course}")

# studentData = Student("Valentine",16,"Male","Dark",1234,"hybrid")
# studentData.display_student()