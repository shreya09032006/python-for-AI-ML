#while loop 
i=0
while i<5:
    print(i)
    i+=1

#reverse loop
i=5
while i>0:
    print(i)
    i-=1    


# print muliplication table of a number
num = int(input("Enter a number: "))
i=1
while i<=10:
    print(num, "x", i, "=", num*i)
    i+=1    

#odd num using continue
i=0
while i<10:
    i+=1
    if i%2==0:
        continue
    print(i)    

# for loop
string = "Hello"
for char in string:
    print(char)    

# print vowel count
word =  "artificial"  
vowel_count = 0
for char in word:
    if char in "aeiouAEIOU":
        vowel_count += 1
print("Number of vowels in the word:", vowel_count) 