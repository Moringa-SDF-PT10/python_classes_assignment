class Person:
    def __init__(self,name,age,gender, complexion):
        self.name = name
        self.age = age
        self.gender = gender
        self.complexion = complexion
    
    def display_info(self):
        print(f"My name is {self.name} and am {self.age} old")

# if __name__ == "__main__":
# personTest = Person("Valentine",16,"Male","Dark")
# print("Student 1 information:")
# personTest.display_info()
