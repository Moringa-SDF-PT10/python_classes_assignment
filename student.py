from person import Person

class Student(Person):
    def __init__(self, student_ID, courses, mode_of_study): #("Full-time"), ("Part-time"), ("Hybrid")#)
        self.student_ID = student_ID
        self.courses = courses
        self.mode_of_study = mode_of_study

   

        

    def enroll (self, course):
        print(f"{self.student_ID} is enrolled to {self.courses} as a  {self.mode_of_study} student.")
        
Python = Student("M1", "Python","Full-time")
Python.enroll(course="Python")
