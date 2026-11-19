#lists

marks = [90, 80, 70, 60, 50]
print(marks)  # Output: [90, 80, 70, 60, 50]
print(marks[0])  # Output: 90
marks[0] = 95
print(marks)  # Output: [95, 80, 70, 60, 50]
print(marks[0:5])  # Output: [95, 80, 70, 60, 50]


# list methods
numbers = [1, 2, 3, 4, 5]
# append method
numbers.append(6)
print(numbers)  # Output: [1, 2, 3, 4, 5, 6]
# insert method     
numbers.insert(2, 10)
print(numbers)  # Output: [1, 2, 10, 3, 4, 5, 6]
# sort method
numbers.sort()
print(numbers)  # Output: [1, 2, 3, 4, 5, 6, 10]
# reverse method
numbers.reverse()
print(numbers)  # Output: [10, 6, 5, 4, 3, 2, 1]

# list loops linear search 
nums = [1,2,3,10,15]

x = 10
idx = 0
for val in nums:
    if val == x:
        print("Found", x, "at index", idx)
        break
    idx += 1


