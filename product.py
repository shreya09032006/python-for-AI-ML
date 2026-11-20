class product:

    count = 0
    def __init__(self, name , price):
        self.name=name
        self.price=price
        product.count += 1

    def get_info(self):
        print(f"price of {self.name} is Rs.{self.price}")

    @classmethod
    def get_count(cls):
        print(f"total products in store = {cls.count}")

    @staticmethod
    def calc_discount(price, discount):
        print(f"discounted price = { price - (price * discount / 100)}")

p1 = product("iphone" , 900000)
p2 = product("macbook" , 700000)       

p1.get_info()
p2.get_info()
p1.calc_discount(10000 , 36)


#oops priciple 

class bankaccount:
    def __init__(self,name, balance):
        self.name = name #public
        self.__balance = balance #private

    def get_balance(self): #getter
        return self.__balance    
    def set_balance(self , newBalance): #setter
        self.__balance = newBalance
acc1 = bankaccount("shreya mhatre" , 10000)   
acc1.set_balance(200_0000)     
print(acc1.name , acc1.get_balance())
#print(acc1.bankaccount__balance) -> data mangling 
#data mangling -> Data mangling (also called name mangling) in Python is a process in which Python automatically changes the name of a class attribute that starts with two underscores (__) by adding the class name as a prefix


#inheritance 

class employee:
    start_time = "10am"
    end_time = "6pm"
    def change_time(self, new_end_time):
           self.end_time = new_end_time

class teacher(employee):
    def __init__(self,subject):
        self.subject = subject

class adminstaff(employee):
    def __init__(self,role):
        self.role = role


t1 = teacher("maths")
t1.change_time("7pm")

print(t1.subject ,t1.start_time , t1.end_time)


#multilevel of inheritance 

class Employee:
    start_time = "10am"
    end_time = "6pm"
class Adminstaff(Employee):
    def __init__(self,role):
        self.role = role
class accountant(Adminstaff):
    def __init__(self , salary , role):
        super().__init__(role)
        self.salary = salary

acc1 = accountant(25_000 , "ca")

print(acc1.role , acc1.salary , acc1.start_time , acc1.end_time)

#multiple level of inheritance 

class Teacher:
    def __init__(self,salary):
        self.salary = salary
class Student:
    def __init__(self,cgpa):
        self.cgpa = cgpa
class TA(Teacher , Student):
    def __init__(self , salary , cgpa ,name):
       super().__init__(salary)
       Student.__init__(self, cgpa)
       self.name = name                
ta1 = TA(15_000 , 9.3 , "shreya")

print(ta1.name ,  ta1.salary , ta1.cgpa)