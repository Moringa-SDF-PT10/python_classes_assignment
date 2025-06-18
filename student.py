import person
from person import Person

class Student(Person):
    def __init__(self, name, age, gender, complexion, student_id, mode_of_study):
        super().__init__(name, age, gender, complexion)
        self.student_id = student_id
        self.mode_of_study = mode_of_study
        self.courses = []

    def enroll(self, course):
        if course not in self.courses:
            self.courses.append(course)

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"student_id: {self.student_id}")
        print(f"courses: {self.courses}")
        print(f"mode_of_study: {self.mode_of_study}")

Valentine = Student("Valentine", "20", "Female", "Brown", "1240", "Part_Time")
Valentine.enroll("Software_Engineering")
Valentine.display_info()



        


    
    

 
