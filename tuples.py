#tuples

tuple1 = (1, 2, 3, 4, 5)
print(tuple1)  # Output: (1, 2, 3, 4, 5)
print(tuple1[0])  # Output: 1   
print(len(tuple1))  # Output: 5
print(tuple1[1:4])  # Output: (2, 3, 4)

#looping through a tuple
for val in tuple1:
    print(val)  # Output: 1 2 3 4 5

#sum 

sum = 0
for val in tuple1:
    sum += val
print("Sum of tuple elements:", sum)  # Output: Sum of tuple elements:


#methods
tuple2 = (6, 7, 8, 9, 10)
#index method
print(tuple2.index(8))  # Output: 2
#count method
print(tuple2.count(7))  # Output: 1
