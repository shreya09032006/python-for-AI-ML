#constructor

class Student:
    def __init__(self,name,cgpa):
        self.name=name
        self.cgpa=cgpa
stu1 = Student("rahul", 9.2)
stu2 = Student("shreya", 9.3)      

print(stu1.name )
print(stu1.cgpa)