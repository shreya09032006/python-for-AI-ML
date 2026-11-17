#7
celsiusTemp = input("Enter temperature in Celsius: ")
fahrenheitTemp = (float(celsiusTemp) * 9/5) + 32
print(celsiusTemp, "Celsius is equal to", fahrenheitTemp, "Fahrenheit") 

#8
radius = float(input("Enter the radius of the circle: "))
area = 3.14 * radius ** 2
print("The area of the circle with radius", radius, "is:", area)

#9

P = int(input("Enter the principal amount: "))
R = int(input("Enter the rate of interest: "))
T = int(input("Enter the time in years: "))
P , R , T = float(P) , float(R) , float(T)
SI = (P * R * T) / 100
print("The simple interest for principal amount", P, "at rate of interest", R, "for time period", T, "years is:", SI) 

#10
decimalNum = float(input("Enter a decimal number: "))
intPart = int(decimalNum)
decimalPart = decimalNum - intPart
print("The integer part of", decimalNum, "is:", intPart)
print("The decimal part of", decimalNum, "is:", decimalPart)




