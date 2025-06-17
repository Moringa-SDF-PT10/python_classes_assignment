class Person:
    def __init__(self, name, age, gender, complexion):
        pass
        self.name = name
        self.age = age
        self.gender = gender
        self.complexion = complexion 

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


joseph = Person(name="joseph", age= 29, gender= "male", complexion= "dark")