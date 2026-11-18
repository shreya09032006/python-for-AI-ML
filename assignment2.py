#1
salary = float(input("Enter your salary: "))
if salary < 30000:
     final_tax_rate = salary * 0.05
     print("Your tax rate is 5% and your final tax is:", final_tax_rate)
elif salary >= 30000 and salary <= 70000:
     final_tax_rate = salary * 0.15 
     print("Your tax rate is 15% and your final tax is:", final_tax_rate)
elif salary > 70000:
     final_tax_rate = salary * 0.25
     print("Your tax rate is 25% and your final tax is:", final_tax_rate)   


#2
def evenodd(num1,num2):
    for i in range(num1,num2+1):
        if i%2==0:
            print(i,"is even")
        elif i%2!=0:
            continue 
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
evenodd(num1,num2)

#3
def digit(num):
    while num > 0:
        d = num % 10
        print(d)
        num = num // 10

digit(312)

#4
def count(num):
    count=0
    while num > 0:
        count += 1
        num = num // 10
    return count

print(count(312))


#5
def sum(num):
    sum=0 
    while num > 0:
        d = num % 10
        sum += d
        num = num // 10
    return sum

print(sum(312))