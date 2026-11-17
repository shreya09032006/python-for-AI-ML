username = input("Enter your username: ")
password = input("Enter your password: ")
if username == "admin" and password == "password123":
    print("Login successful!")
else:
    print("Login failed. Please check your username and password.")


num = int(input("Enter a number: "))
if (num % 5 == 0):
    print(num, "is divisible by 5.")
else:
    print(num, "is not divisible by 5.")