#6
for i in range ( 1, 101):
    if i%3==0 and i%5==0:
        print(i)
    else:       
        continue

#7 

while True:
    n = input("Enter a number (or 'quit' to exit): ")

    if n.lower() == "quit":
        break

    n = float(n)

    if n > 0:
        print("Positive")
    elif n < 0:
        print("Negative")
    else:
        print("Zero")
#8
def calculate(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operator"

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /): ")
result = calculate(num1, num2, operator)
print("Result:", result)

#9

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


print(is_prime(9))
print(is_prime(7))


