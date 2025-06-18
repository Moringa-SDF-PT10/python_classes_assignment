from main import Person
from mentor import Mentor
from student import Student

def main():
    print("=== PERSON ===")
    person1 = Person("Jane Doe", 30, "Female", "Medium")
    person1.display_info()
    
    print("\n=== STUDENT ===")
    student1 = Student("Alice Johnson", 22, "Female", "Light", "STD123", "Full-time")
    student1.enroll("Python Programming")
    student1.enroll("Data Science")
    student1.display_info()
    
    print("\n=== TECHNICAL MENTOR ===")
    mentor1 = Mentor("John Smith", 35, "Male", "Dark", "EMP456", "Part-time")
    mentor1.assign_course("Python Programming")
    mentor1.assign_course("Web Development")
    mentor1.display_info()

if __name__ == "__main__":
    main()