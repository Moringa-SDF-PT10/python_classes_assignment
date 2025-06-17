import unittest
from school_system import Person

class TestPerso(unittest.TestCase):
    
    def setUp(self):
        self.joseph = Person(name="joseph", age= 29, gender= "male", complexion= "dark")

    def test_student_name(self):
        self.assertEqual(self.joseph.name, "joseph")

if __name__ == "__main__":
    unittest.main()