#pallindrome string
string = input("Enter a string: ")

reverse = string[::-1]

if string == reverse:
    print("It is a palindrome")
else:
    print("It is not a palindrome")

# avg of list 
list = [10, 20, 30, 40, 50]
avg = sum(list) / len(list)
print("Average of the list is:", avg)

#list conactenation
list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated_list = list1 + list2
print("Concatenated list:", concatenated_list)

#4
tuple = (1,2,3,4,5,6,7,8,9,10)
even = ()
odd = ()
for i in tuple:
    if i % 2 == 0:
        even += (i,)
    else:
        odd += (i,)
print("Even numbers:", even)
print("Odd numbers:", odd)        

#5

students = {}

while True:
    print("\n----- STUDENT DATABASE -----")
    print("A. Add a student")
    print("B. Update marks")
    print("C. Search for a student")
    print("D. Display all students")
    print("E. Exit")

    choice = input("Enter your choice: ").upper()

    if choice == "A":
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))

        students[name] = marks
        print("Student added successfully!")

    elif choice == "B":
        name = input("Enter student name: ")

        if name in students:
            marks = int(input("Enter updated marks: "))
            students[name] = marks
            print("Marks updated successfully!")
        else:
            print("Student not found!")

    elif choice == "C":
        name = input("Enter student name: ")

        if name in students:
            print("Marks:", students[name])
        else:
            print("Student not found!")

    elif choice == "D":
        if len(students) == 0:
            print("No students available!")
        else:
            for name, marks in students.items():
                print(name, ":", marks)

    elif choice == "E":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again.")
