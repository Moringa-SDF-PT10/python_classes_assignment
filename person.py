class Person:
    def __init__(self, name, age, gender , complexion="dark"):
        self.name = name
        self.age = age
        self.gender= gender
        self.complexion = complexion

        
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age} , Complexion: {self.complexion}")

Rowney = Person("Rowney", 30, "male", "fair")  
Rowney.display_info() 

Gregory= Person ("Gregory", 20, "male", "dark")
Gregory.display_info()

Githu = Person("Githu", 25, "Male" , "dark")

