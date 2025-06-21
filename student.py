from school_system import Person

class Student(Person):
    def __init__(self, name, age, gender, complexion, student_id, courses, mode_of_study, year_of_study):
        super().__init__(name, age, gender, complexion)
        self.student_id = student_id
        self.courses = courses
        self.mode_of_study = mode_of_study
        self.year_of_study = year_of_study

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
        
joseph = Student ("Joseph", 23, "male", "dark", "MR-001", ["HTML", "CSS", "JavaScript"], "online", 1)
# print(joseph.student_id)
# print(joseph.courses)
# print(joseph.mode_of_study)
# print(joseph.year_of_study)
# print(joseph.name)
# print(joseph.display_info())
