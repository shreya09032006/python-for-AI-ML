#print sum of firt n natural numbers
n = int(input("Enter a number: "))
sum = 0
for i in range(1, n+1):
    sum += i
print("Sum of first", n, "natural numbers is:", sum)

#functions
def avg(num1, num2 , num3 ):
    return (num1 + num2 + num3) / 3

print("Average of 10, 20, 30 is:", avg(10, 20, 30))

#lambda function
sum = lambda a, b: a + b
print("Sum of 5 and 10 is:", sum(5, 10))

#factorial
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

print("Factorial of 5 is:", factorial(5))
