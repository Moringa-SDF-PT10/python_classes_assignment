from .interface import SchoolManagementSystem

def main():
    system = SchoolManagementSystem()
    
    while True:
        print("\n1. Add Student\n2. Add Mentor\n3. View All\n4. Exit")
        choice = input("Choose option: ")
        
        if choice == "1":
            data = {
                'name': input("Name: "),
                'age': int(input("Age: ")),
                'gender': input("Gender: "),
                'complexion': input("Complexion: "),
                'student_id': input("Student ID: "),
                'mode_of_study': input("Mode of Study: ")
            }
            print(system.add_student(data))
        
        elif choice == "2":
            data = {
                'name': input("Name: "),
                'age': int(input("Age: ")),
                'gender': input("Gender: "),
                'complexion': input("Complexion: "),
                'employee_id': input("Employee ID: "),
                'mode_of_teaching': input("Mode of Teaching: ")
            }
            print(system.add_mentor(data))
        
        elif choice == "3":
            system.display_all()
        
        elif choice == "4":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()