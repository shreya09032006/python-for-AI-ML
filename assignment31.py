#6
words = ["apple", "banana", "kiwi", "cherry", "mango"]
dict = {}

for val in words:
    dict[val] = len(val)

print(dict)    

#7

string = input("enter your string :")

count = 0 
for ch in string:
    if( ch == " "):
        count += 1
        print(count)

#8
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

set1 = set(list1)
set2 = set(list2)

result = set1.intersection(set2)

print(result)

#9
list = ["shreya", "krrish" , "anirudh" , "krrish"]
set1 = set(list)
print(set1)

#10

string = input("Enter a string: ")

unique = set(string)

print("All unique characters:", unique)
print("Count of unique characters:", len(unique))

