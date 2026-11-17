#1
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print("Hello", name, "you are", age, "years old.") 

#2
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("The sum of", num1, "and", num2, "is:", num1 + num2)
print("The difference of", num1, "and", num2, "is:", num1 - num2)
print("The product of", num1, "and", num2, "is:", num1 * num2)
print("The division of", num1, "and", num2, "is:", num1 / num2) 

#3
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = float(input("Enter third number: "))
avg = float(num1 + num2 + num3) / 3
print("The average of", num1, ",", num2, "and", num3, "is:", avg)

#4

strNum = input("Enter a number: ")
num = int(strNum)
num1 = float(strNum)
print("The number is:", num)
print("The number as a float is:", num1)
num2 = str(num)
print("The number as a string is:", num2) 

#5
x = 10 + 3 * 2 ** 2
print("The value of x is:", x)

#6 swap numbers 
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Before swapping: num1 =", num1, "num2 =", num2)
num1, num2 = num2, num1
print("After swapping: num1 =", num1, "num2 =", num2)
