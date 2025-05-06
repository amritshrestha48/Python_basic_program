#1. Find Even Numbers in a Given Range. #2,4,6,8,10,12,14,16,18,20
'''for num in range(1,21): 
    if num % 2 == 0:  #check if num is even
        print(num)'''

#2. Find odd numbers in a given range. #1,3,5,7,9,11,13,15,17,19,21
'''for num in range(1,21):
    if num % 2 != 0:   #check if num is odd
        print(num, end = " ")'''

#3. Check if a Number is Even or Odd. #2 is even and 3 is odd
'''num = int(input("Enter a number: "))
if num % 2 == 0:
    print("even Number")
else:
    print(f"{num} is odd number")'''


#4.  Find the Largest Number in a List. #50 is Largest number
'''numbers = [10, 25, 30, 5, 50]
print("Largest number:", max(numbers))'''

#5. Reverse a String # "Python" to "nohtyp"
'''text = "Python" 
print("Reversed:", text[::-1])''' 

#6. Write a program to do arthmetical operations addition and division.
#Addition. #2+3=5
'''num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
sum = num1 + num2  #addition
print("Sum:", sum)
'''
#Division. #10/2=5.0
'''num1 = float(input("Enter dividend number: "))
num2 = float(input("Enter divisor number:"))
if num2 == 0:
    print("Error: Division by zero is not allowed.")
else:
    result = num1 / num2
    print("Result:", result)'''

#7. write a program to find the area of a traingle. #area = 0.5 * base * height
'''base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the traingle: "))
area = 0.5 * base * height  #area of triangle
print("Area of the triangle:", area)'''

#8. write a program to find the area of a circle. #area = pi * r^2
'''import math
radius = float(input("Enter the radius of the circle: "))
area = math.pi * radius ** 2  #area of circle
print("Area of the circle:", area)'''

#9. write a program to swap two variables.  #swap a=5, b=8 to a=8, b=5
'''a = int(input("Enter firt number: :"))
b = int(input("Enter second number: "))
print(f"Before swapping: a = {a}, b = {b}")
temp = a #swap the value using temp variable
a = b
b = temp
print(f"After swapping: a = {a}, b = {b}")'''

#10. write a program to find the factorial of a number. #4!= 4*3*2*1=24
'''num = int(input("Enter a number: "))
factorial = 1
for i in range (1, num + 1):  #loop from 1 to num
    factorial *= i  #multiply the numbers from 1 to num
    print(f"Factorial of {num} is {factorial}")'''
          
#or
'''import math
num = int(input("Enter a number: "))
factorial = math.factorial(num) #using math module to find factorial
print(f"Factorial of {num} is {factorial}")'''

#11. write a program to generate a random number. #1-100
'''import random 
print(f"Random number: {random.randint(1, 100)}")'''  

#12. write a program to convert kilometer to miles. #1km = 0.621371miles
''''kilometers = float(input("Enter distance in Kilomters: "))
miles = kilometers * 0.621371 #conversion factor
print(f"{kilometers} kilometers is equal to {miles} miles")'''

#13. write  a program to convert celsius to farenheit. #(C * 9/5) + 32 = F
'''celsius = float(input("Enter temperature in Celsius: "))
farenheit = (celsius * 9/5) + 32  #conversion formula
print(f"{celsius} Celsious is equal to {farenheit} Farenheit")'''

#14. write a program to convert farenheit to celsius. #(F - 32) * 5/9 = C
'''farenheit = float(input("Enter temperature in Farenheit: "))
celsius = (farenheit - 32) * 5/9 #conversion formula
print(f"{farenheit} Farenheit is equal to {celsius} Celsius")'''

#15. write a program to display calender. #2024-01
'''import calendar
year = int(input("Enter year: "))
month = int(input("Enter month: ")) 
print(calendar.month(year, month)) #display the calender of the month and year''' 

#16. write a program to check if a number is prime or not. #2,3,5,7,11 are prime numbers
'''num = int(input("Enter a number: "))
if num > 1:                   #check if num is greater than 1
    is_prime = True           #assume num is prime
    for i in range(2, num):   #loop from 2 to num-1
        if num % i == 0:      #check if num is divisible by i
            is_prime = False  #num is not prime
            break
    if is_prime:
        print(num, "is a prime number")
    else:
        print(num, "is not a prime number")
else:
    print(num, "is not a prime number")'''

#17. write a program to check if a number is palindrome or not. #121, 12321 are palindrome numbers
'''num = int(input("Enter a number: "))          
reverse = 0
temp = num

while temp > 0:                      #loop until temp is greater than 0
    digit = temp % 10                #get the last digit of temp
    reverse = reverse * 10 + digit   #update reverse
    temp = temp // 10                #remove the last digit from temp
 
if num == reverse:                   #check if num is equal to reverse
        print(num, "is a palindrome")
else:
        print(num, "is not a palindrome")'''

#18. write a program to solve quadratic equation. #ax^2 + bx + c = 0
'''import cmath

#input coefficients
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

#calculate discriminant
discriminant = b ** 2 - 4 * a * c
#Check if discriminant is positive, negative or zero
if discriminant > 0: 
    #two real and distnict roots
    root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
    print("Roots are real and different")
    print(f"Root 1: {root1}")
    print(f"Root 2: {root2}")
elif discriminant == 0:
    #one real root
    root = -b / (2 * a)
    print("roots are real and same")
    print("Root: {root}")
else:
    #roots are complex
    real_part = -b / (2 * a)
    imaginary_part = cmath.sqrt(-discriminant) / 2 * a
    root1 = complex(real_part, imaginary_part) 
    root2 = complex(real_part, -imaginary_part)
    print("Roots are complex and different")
    print(f"Root 1: {root1}")
    print(f"Root 2: {root2}")'''
    

#18. write a program to swap two variables without temp variable. #swap a=5, b=8 to a=8, b=5
'''a= 5
b = 8

#Swapping using arithmetic operations
a, b = b, a #swapping using tuple unpacking

print("After swapping: a =", a, ", b =", b)'''

#19. write aprogram to check if a number is Positive, Negative, or Zero. #-5 is negative, 0 is zero, 5 is positive
'''num = float(input("Enter a number:"))
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative numnber")'''

#20. Write a program to check leap year. #2020 is leap year, 2021 is not leap year
'''year = int(input("Enter a year: "))
#divided by 4 and not divided by 100 or divided by 400 means leap year.
if (year %4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year")
else:
    print(year, "is not a Leap year")'''

#21. write a program to print all prime numbers in an interval of 1-10. #2,3,5,7 are prime numbers
'''start = 1
end = 10
for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            #check if num is divisible by i
            if num % i == 0:
                break
        else:
            print(num)'''

#22. write a program to display the multiplication table. #2*1=2 to 2*10=20
'''num = int(input("Display multiplication table of: "))
for i in range(1, 11):
    print(f"{num} * {i} = {num * i}")''' 

#23. write a program to print fibonacci series. # 0,1,1,2,3,5,8,13,21
'''n = int(input("Enter the number of terms: "))
a, b = 0, 1 #Fibonacci series starts with 0 and 1
print("Fibonacci series:")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b #update the values of a and b'''

#24. write a program to check Armstrong number. # 153 = 1^3 + 5^3 + 3^3
'''num = int(input("Enter a number: "))
sum = 0    #initialize sum to 0
temp = num #store the original number

while temp > 0:
    digit = temp % 10   #get the last digit of temp
    sum += digit ** 3   #add the cube of the digit to sum
    temp = temp // 10   #remove the digit from temp

if num == sum: #check if num is equal to sum
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")'''

#25. write a program to find the sum of digits of a number. #123=1+2+3=6
'''num = int(input("Enter a number:"))
sum = 0
while num > 0:
    digit = num % 10  #get the last digit of sum
    sum +=digit       #add the digit to sum
    num = num // 10   #remove the last digit from num

print("Sum of digits:", sum) #display the sum of digits'''

#26. write a program to find the GCD/HCF(greatest common divisor/Highest common factor )  of two numbers. #GCD of 12 and 15 is 3
'''import math
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
gcd = math.gcd(num1, num2)  #using math module to find GCD

print("GCD is:", gcd)       #display the GCD of two numbers'''

#27. write a program to find the LCM(least common multiple) of two numbers. #LCM of 12 and 15 is 60
'''import math
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
lcm = (num1 * num2) // math.gcd(num1, num2) #using math mnodule to find LCM

print("LCM is:", lcm)'''

#28. write a program to find the sum of n natural numbers. #1+2+3+4+5=15
n = int(input("Enter a number: "))

sum_natural_numbers = n * (n + 1) // 2 #sum of n natural numbers formula

print("Sum of first", n, "natural numbers is:", sum_natural_numbers)
