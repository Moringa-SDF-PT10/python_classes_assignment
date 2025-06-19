from .models import Student, TechnicalMentor

class SchoolManagementSystem:
    def __init__(self):
        self.students = []
        self.mentors = []
    
    def add_student(self, student_data):
        student = Student(**student_data)
        self.students.append(student)
        return f"Student {student.name} added"
    
    def add_mentor(self, mentor_data):
        mentor = TechnicalMentor(**mentor_data)
        self.mentors.append(mentor)
        return f"Mentor {mentor.name} added"
    
    def display_all(self):
        print("\nSTUDENTS:")
        for student in self.students:
            student.display_info()
        
        print("\nMENTORS:")
        for mentor in self.mentors:
            mentor.display_info()