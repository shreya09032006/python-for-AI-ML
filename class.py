#constructor

'''class Student:
    def __init__(self,name,cgpa):
        self.name=name
        self.cgpa=cgpa
stu1 = Student("rahul", 9.2)
stu2 = Student("shreya", 9.3)      

print(stu1.name )
print(stu1.cgpa)'''


class Laptop:
    storage_type = "ssd"

    def __init__(self,ram,storage):
        self.ram=ram
        self.storage=storage

    @classmethod
    def get_storage_type(cls):
        print(f"storage type = {cls.storage_type}") 

    def get_info(self):
        print(f"laptop has {self.ram} & {self.storage} {self.storage_type}")

    @staticmethod
    def calc_discount(price,discount):
        final_price = price - (discount * price / 100 )
        print(f"discount price = { final_price }")    

l1 = Laptop("16gb" , "512gb")        


l1.get_info()
l1.get_storage_type()
Laptop.get_storage_type()

l1.calc_discount(40_000 ,10 )