from abc import ABC , abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound():
        pass
class Lion(Animal):
    def make_sound(self):
        print("Roar")

class Cow(Animal):
    def make_sound(self):
        print("muu")


lion = Lion()
lion.make_sound()      

cow = Cow()
cow.make_sound()


#polymorphism 

#operand overlading 

print(1+2 , "shreya" + "mhatre")

#actual polymorphism , function overiding

class Employee:
    def get_designation(self):
        print("designation = employeee")

class Teacher(Employee):
    def get_designation(self):
        print("designation = Teacher")

class Accountant:
    def get_designation(self):
        print("designation = Accountant")

t1 = Teacher()
t1.get_designation()


#duck typing

acc1 = Accountant()
acc1.get_designation()

        