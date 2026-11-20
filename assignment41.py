#6 abstraction 
from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass


class Intern(Employee):
    def calculate_salary(self):
        print("Intern Salary: 10000")


class FullTimeEmployee(Employee):
    def calculate_salary(self):
        print("Full Time Salary: 50000")


class ContractEmployee(Employee):
    def calculate_salary(self):
        print("Contract Salary: 20000")


e1 = Intern()
e2 = FullTimeEmployee()
e3 = ContractEmployee()

e1.calculate_salary()
e2.calculate_salary()
e3.calculate_salary()


#7 multiple inheritance 
class Herbivore:
    def eat_plants(self):
        print("Eats plants")


class Carnivore:
    def eat_meat(self):
        print("Eats meat")


class Omnivore:
    def eat_both(self):
        print("Eats plants and meat")


class Bear(Herbivore, Carnivore, Omnivore):
    def show(self):
        print("Bear can eat different types of food")


b = Bear()

b.show()
b.eat_plants()
b.eat_meat()
b.eat_both()

#8 constructor overloading 
class Person:
    def __init__(self, name, age=0, address="Not given"):
        self.name = name
        self.age = age
        self.address = address

    def display(self):
        print(self.name, self.age, self.address)


p1 = Person("Rahul")
p2 = Person("Amit", 20)
p3 = Person("Shreya", 19, "Mumbai")

p1.display()
p2.display()
p3.display()

#9 instance and class attribute
class Player:
    player_count = 0

    def __init__(self, name, level):
        self.name = name
        self.level = level
        Player.player_count += 1

    def display(self):
        print(self.name, self.level)


p1 = Player("Rahul", 1)
p2 = Player("Amit", 2)
p3 = Player("Shreya", 3)

p1.display()
p2.display()
p3.display()

print("Total players:", Player.player_count)

#10 OOp chat system 
class User:
    def __init__(self, name):
        self.name = name


class Message:
    def __init__(self, sender, text):
        self.sender = sender
        self.text = text

    def display(self):
        print(self.sender, ":", self.text)


class ChatRoom:
    def __init__(self):
        self.users = []
        self.messages = []

    def join(self, user):
        self.users.append(user)
        print(user.name, "joined the chat")

    def leave(self, user):
        self.users.remove(user)
        print(user.name, "left the chat")

    def send_message(self, user, text):
        msg = Message(user.name, text)
        self.messages.append(msg)

    def chat_history(self):
        print("\nChat History:")
        for msg in self.messages:
            msg.display()



# Creating users
u1 = User("Rahul")
u2 = User("Amit")

# Creating chatroom
room = ChatRoom()

# Users joining
room.join(u1)
room.join(u2)

# Sending messages
room.send_message(u1, "Hello!")
room.send_message(u2, "Hi Rahul!")

# Viewing chat history
room.chat_history()

# User leaving
room.leave(u2)