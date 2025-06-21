import unittest
from student import Student
from technical_mentor import TechnicalMentor

class TestPerson(unittest.TestCase):
    
    def setUp(self):
        self.student = Student("Joseph", 23, "male", "dark", "MR-001", ["HTML", "CSS", "JavaScript"], "online", 1)
        self.mentor = TechnicalMentor("Charles", 30, "male", "brown", "MTM-001", ["HTML", "CSS", "JavaScript"], "online")

    def test_student_enrollment (self):
        self.student.enroll("CSS")
        self.assertIn("CSS", self.student.courses)

    def test_student_enrollment_duplicate(self):
        self.student.enroll("HTML")
        self.assertEqual(self.student.courses.count("HTML"), 1)

    def test_mentor_course_assignment(self):
        self.mentor.assign_course("JavaScript")
        self.assertIn("JavaScript", self.mentor.courses)

    def test_mentor_course_assignment_duplicate(self):
        self.mentor.assign_course("python")
        self.assertEqual(self.mentor.courses.count("Python"), 1)

    def test_student_display_info(self):
        self.student.display_info() # ensuring no error is raised

    def test_mentor_display_info(self):
        self.mentor.display_info() # ensuring no error is raised

    def test_invalid_mode_of_study(self):
        student1 = Student("Maureen", 24, "female", "chocolate", "MS-002", ["HTML"], 1, mode_of_study="part-time-remote")
        self.assertEqual(student1.mode_of_study, "part-time-remote") # valid modes can later be restricted

    def test_negative_age(self):
        student2 = Student("Brian", -5, "Male", "Dark", "MS-003", [], "online", 1)
        self.assertEqual(student2.age, -5)

if __name__ == "__main__":
    unittest.main()