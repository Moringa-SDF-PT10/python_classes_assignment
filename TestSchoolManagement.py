import unittest
from Person import Person
from Student import Student
from TechnicalMentor import TechnicalMentor

class TestSchoolManagement(unittest.TestCase):
    def test_person_attributes(self):
        p = Person("Alice", 30, "Female", "Fair")
        self.assertEqual(p.name, "Alice")
        self.assertEqual(p.age, 30)
        self.assertEqual(p.gender, "Female")
        self.assertEqual(p.complexion, "Fair")

    def test_student_enroll_and_display(self):
        s = Student("Bob", 20, "Male", "Dark", "S123", "Full-time")
        self.assertEqual(s.courses, [])
        s.enroll("Math")
        self.assertIn("Math", s.courses)
        s.enroll("Math")  # Should not duplicate
        self.assertEqual(s.courses.count("Math"), 1)
        s.enroll("Science")
        self.assertIn("Science", s.courses)

    def test_student_invalid_enroll(self):
        s = Student("Carol", 22, "Female", "Light", "S456", "Hybrid")
        s.enroll(123)  # Enroll with non-string
        self.assertIn(123, s.courses)  # Accepts any type, but let's check

    def test_student_display_info(self):
        s = Student("Dan", 19, "Male", "Medium", "S789", "Part-time")
        s.enroll("English")
        # Just check that display_info runs without error
        s.display_info()

    def test_mentor_assign_and_display(self):
        m = TechnicalMentor("Eve", 35, "Female", "Olive", "T001", "Full-time")
        self.assertEqual(m.courses, [])
        m.assign_course("Python")
        self.assertIn("Python", m.courses)
        m.assign_course("Python")  # Should not duplicate
        self.assertEqual(m.courses.count("Python"), 1)
        m.assign_course("Django")
        self.assertIn("Django", m.courses)
        m.display_info()

    def test_mentor_invalid_assign(self):
        m = TechnicalMentor("Frank", 40, "Male", "Tan", "T002", "Part-time")
        m.assign_course(None)
        self.assertIn(None, m.courses)

    def test_edge_cases(self):
        # Negative age
        p = Person("Ghost", -1, "Other", "Unknown")
        self.assertEqual(p.age, -1)
        # Empty name
        s = Student("", 18, "Female", "Fair", "S000", "Hybrid")
        self.assertEqual(s.name, "")
        # Non-string IDs
        s2 = Student("Henry", 21, "Male", "Dark", 999, "Full-time")
        self.assertEqual(s2.student_id, 999)
        m2 = TechnicalMentor("Ivy", 29, "Female", "Light", 123, "Hybrid")
        self.assertEqual(m2.employee_id, 123)

if __name__ == "__main__":
    unittest.main() 