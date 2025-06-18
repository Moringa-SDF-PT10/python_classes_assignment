from main import Person
from mentor import Mentor
from student import Student

def main():
    print("=== PERSON ===")
    person1 = Person("Jane Doe", 30, "Female", "Medium")
    person1.display_info()

if __name__ == "__main__":
    main()