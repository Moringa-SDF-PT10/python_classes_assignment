from person import Person
from student import Student
from technical_mentor import TechnicalMentor

def test_person():
    person=Person("Lucy", 25, "Female", "Fair")
    assert person.name == "Lucy"
    assert person.age == 25
    assert person.gender == "Female"
    assert person.complexion == "Fair"

def test_student():
    person=Student("Valentine", 20, "Female", "Brown","1240", "Part_Time")
    assert person.name == "Valentine"
    assert person.age == 20
    assert person.gender == "Female"
    assert person.complexion == "Brown"
    assert person.student_id == "1240"
    assert person.mode_of_study == "Part_Time"

def test_technical_menntor():
    person=TechnicalMentor("Edgar","25", "Male", "Dark", "4423", "Hybrid")
    assert person.name == "Edgar"
    assert person.age == "25"
    assert person.gender == "Male"
    assert person.complexion == "Dark"
    assert person.employee_id == "4423"
    assert person.mode_of_teaching == "Hybrid"

