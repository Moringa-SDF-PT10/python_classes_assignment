class Person:
    def __init__(self, name, age, complexion, gender = "Prefer not to say"):
        self.name = name
        self.age = age
        self.gender = gender
        self.complexion = complexion

    def display_info(self):
        print(f"Name: {self.name}\nAge: {self.age}")
