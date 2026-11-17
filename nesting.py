username = input("Enter your username: ")
password = input("Enter your password: ")
if username == "admin" and password == "password123":
    print("Login successful!")
else:
    if username != "admin":
        print("Login failed. Incorrect username.")
    elif password != "password123":
        print("Login failed. Incorrect password.")