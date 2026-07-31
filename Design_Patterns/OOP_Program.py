#Class and Object - 
class Student:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("Name:", self.name)

s = Student("Sanket")
s.show()

#Inheritance - 
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.sound()
d.bark()

#Polymorphism - 
class Bird:
    def fly(self):
        print("Bird flies")

class Penguin(Bird):
    def fly(self):
        print("Penguin cannot fly")

b = Bird()
p = Penguin()

b.fly()
p.fly()