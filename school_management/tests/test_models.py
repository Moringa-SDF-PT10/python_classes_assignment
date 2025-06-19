import pytest
from ..models import Student, TechnicalMentor

def test_student_creation():
    s = Student("Alice", 20, "F", "Light", "S001", "Full-time")
    assert s.name == "Alice"
    assert s.enroll("Math") == "Enrolled in Math"
    assert s.enroll("Math") == "Already enrolled in Math"

def test_mentor_creation():
    m = TechnicalMentor("Bob", 30, "M", "Dark", "T001", "Part-time")
    assert m.name == "Bob"
    assert m.assign_course("Python") == "Assigned to teach Python"
    assert m.assign_course("Python") == "Already teaching Python"