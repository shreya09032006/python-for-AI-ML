#1 class & objects 

class BankAccount:

    # Constructor
    def __init__(self, account_number, owner_name, balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    # Deposit money
    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    # Withdraw money
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance!")

    # Check balance
    def check_balance(self):
        print("Account Holder:", self.owner_name)
        print("Account Number:", self.account_number)
        print("Available Balance:", self.balance)


# Creating an object
acc1 = BankAccount(12345, "Shreya", 10000)

acc1.deposit(5000)
acc1.withdraw(2000)
acc1.check_balance()

#2 class & objects 


class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.__reviews = []  # Private attribute

    # Add a new review
    def add_review(self, review):
        self.__reviews.append(review)
        print("Review added successfully!")

    # Count total reviews
    def count_reviews(self):
        return len(self.__reviews)

    # Display all reviews
    def display_reviews(self):
        for review in self.__reviews:
            print("-", review)


# Creating object
b1 = Book("Wings of Fire", "APJ Abdul Kalam")

b1.add_review("Very inspiring book")
b1.add_review("Must read for students")
b1.add_review("Great life lessons")

print("Total reviews:", b1.count_reviews())

print("All reviews:")
b1.display_reviews()


#3 encaplusation 
class Student:
    def __init__(self, name, roll_no, marks):
        self.__name = name
        self.__roll_no = roll_no
        self.__marks = marks

    # Getter methods
    def get_name(self):
        return self.__name

    def get_roll_no(self):
        return self.__roll_no

    def get_marks(self):
        return self.__marks

    # Setter methods
    def set_name(self, name):
        if name != "":
            self.__name = name
        else:
            print("Name cannot be empty")

    def set_roll_no(self, roll_no):
        if 1 <= roll_no <= 100:
            self.__roll_no = roll_no
        else:
            print("Roll number must be between 1 and 100")

    def set_marks(self, marks):
        if marks >= 0:
            self.__marks = marks
        else:
            print("Marks cannot be negative")


s1 = Student("Rahul", 10, 85)

print("Name:", s1.get_name())
print("Roll No:", s1.get_roll_no())
print("Marks:", s1.get_marks())

s1.set_marks(-5)
s1.set_roll_no(150)
s1.set_name("")

#4 function overding 
class Shape:
    def area(self):
        print("Area of shape")


class Circle(Shape):
    def area(self):
        r = 5
        print("Area of Circle:", 3.14 * r * r)


class Rectangle(Shape):
    def area(self):
        l = 10
        b = 5
        print("Area of Rectangle:", l * b)


class Triangle(Shape):
    def area(self):
        h = 8
        b = 6
        print("Area of Triangle:", 0.5 * b * h)


c = Circle()
r = Rectangle()
t = Triangle()

c.area()
r.area()
t.area()

#5 inheritance 
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


class Car(Vehicle):
    def __init__(self, brand, model, seats):
        super().__init__(brand, model)
        self.seats = seats


class Bike(Vehicle):
    def __init__(self, brand, model, engine_cc):
        super().__init__(brand, model)
        self.engine_cc = engine_cc


c = Car("Tata", "Nexon", 5)
b = Bike("Royal Enfield", "Classic", 350)

print("Car:", c.brand, c.model, c.seats)
print("Bike:", b.brand, b.model, b.engine_cc)


