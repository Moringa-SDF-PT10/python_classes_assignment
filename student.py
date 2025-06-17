from school_system import Person

class Student(Person):
    def __init__(self, student_id, courses, mode_of_study):
        self.student_id = student_id
        self.courses = []
        self.mode_of_study = mode_of_study

    def enroll(self, course):
        if course in self.courses:
            print(f"Already enrolled in {course}.")
        else:
            self.courses.append(course)

    def display_info(self):
           super().display_info()
           print(
                f"Student ID: {self.student_id}\n"
                f"Mode of Study: {self.mode_of_study}\n"
                f"Courses: {self.courses}"
           )
        
joseph = Student