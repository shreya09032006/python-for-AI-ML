word1 = "Hello"
word2 = "World"
# Concatenating the two words with a space in between
result = word1 + " " + word2
print(result)  # Output: Hello World
print("Length of the result:", len(result))  # Output: Length of the result: 11

#slicing
str = "python"
print(str[2:4])  # Output: th
print(str[:3])   # Output: pyt
print(str[3:])   # Output: hon
print(str[-4:-2])  # Output: th

# string formatting
a = 10
b = 20
sum = a + b
print("The sum of {} and {} is {}".format(a, b, sum))

# index formatting
print("The sum of {0} and {1} is {2}".format(a, b, sum))  # Output: The sum of 10 and 20 is 30

#value based formatting
print("the sum of vars {a} and {b} is {sum}".format(a=10, b=20, sum=30))  # Output: The sum of vars 10 and 20 is 30

#f-strings
a = 10
b = 20
print(f"The sum of {a} and {b} is {a + b}")  # Output: The sum of 10 and 20 is 30