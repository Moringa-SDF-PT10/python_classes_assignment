import pytest
from person import Person, Student, TechnicalMentor


class TestPerson:
    def setup_method(self):
        self.person = Person(name="John", age=20, gender="M", complexion="dark")

    def test_initial_name(self):
        assert self.person.name == "John"

    def test_initial_age(self):
        assert self.person.age == 20

    def test_initial_gender(self):
        assert self.person.gender == "M"

    def test_initial_complexion(self):
        assert self.person.complexion == "dark"

    def test_display_info(self):
        assert "name: John age: 20" in self.person.display_info()


class TestStudent:
    def setup_method(self):
        self.student = Student(
            name="John",
            age=20,
            gender="M",
            complexion="dark",
            student_id="S003/2025",
            mode_of_study="part_time",
            courses=["JS, Python"],
        )

    def test_initial_name(self):
        assert self.student.name == "John"

    def test_initial_age(self):
        assert self.student.age == 20

    def test_initial_gender(self):
        assert self.student.gender == "M"

    def test_initial_complexion(self):
        assert self.student.complexion == "dark"

    def test_initial_student_id(self):
        assert self.student.student_id == "S003/2025"

    def test_initial_mode_of_study(self):
        assert self.student.mode_of_study == "part_time"

    def test_initial_courses(self):
        assert self.student.courses == ["JS, Python"]

    def test_display_info(self):
        assert (
            self.student.display_info()
            == "name: John age: 20 student_id: S003/2025 mode_of_study: part_time courses: ['JS, Python']"
        )

    def test_enroll_course(self):
        self.student.enroll("React")
        assert self.student.courses == ["JS, Python", "React"]


class TestTechnicalMentor:
    def setup_method(self):
        self.technical_mentor = TechnicalMentor(
            name="John",
            age=20,
            gender="M",
            complexion="dark",
            employee_id="E003/2025",
            mode_of_teaching="part_time",
            courses=["JS, Python"],
        )

    def test_initial_name(self):
        assert self.technical_mentor.name == "John"

    def test_initial_age(self):
        assert self.technical_mentor.age == 20

    def test_initial_gender(self):
        assert self.technical_mentor.gender == "M"

    def test_initial_complexion(self):
        assert self.technical_mentor.complexion == "dark"

    def test_initial_employee_id(self):
        assert self.technical_mentor.employee_id == "E003/2025"

    def test_initial_mode_of_teaching(self):
        assert self.technical_mentor.mode_of_teaching == "part_time"

    def test_initial_courses(self):
        assert self.technical_mentor.courses == ["JS, Python"]

    def test_display_info(self):
        assert (
            self.technical_mentor.display_info()
            == "name: John age: 20 employee_id: E003/2025 mode_of_teaching: part_time courses: ['JS, Python']"
        )

    def test_assign_course(self):
        self.technical_mentor.assign_course("React")
        assert self.technical_mentor.courses == ["JS, Python", "React"]
