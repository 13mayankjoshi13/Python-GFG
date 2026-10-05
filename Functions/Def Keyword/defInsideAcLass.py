class Person:
    def __init__(self, name, age):
        self.name = name  
        self.age = age    
    
    def greet(self):
        print(f"Name - {self.name} and Age - {self.age}.")

p1 = Person("Harry", 30)
p1.greet()