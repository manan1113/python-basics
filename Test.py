# # Que 1  Write a Python program to take an integer, float, and string input from the user and print them
#  using f-string.
# a = int(input("enter your number :"))
# b = float(input("enter your number :"))
# c = str(input("enter your number :"))

# print(f"Integer value is", a)
# print(f"Float value is", b)
# print(f"String value is", c)


#Que 2 . Write a program to check the type of variables: integer, float, string, list, tuple, dictionary.
# a = 10                 
# b = 10.2              
# c = "Hello"            
# d = [1, 2, 3, 4, 5]        
# e = (5, 6, 7, 8)           
# f = {"name": "Prabh", "age": 17}  

# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))
# print(type(f))


#Que 3  Write a program that takes two numbers as input and prints their sum, difference, product, and
#  division.
# a = int(input("Enter your first number :"))
# b = int(input("enter your second number :"))
# print("Sum is", a+b)
# print("Diff is", a-b)
# print("product is", a*b)
# print("Division is", a/b)


#Que 4  Write a program that converts Celsius to Fahrenheit.
# c = float(input("Enter temperature in Celsius: "))
# def temp_converter(celsius):
#     return (celsius * 9/5) + 32

# f = temp_converter(c)
# print("Temp in farenhite is", f)


# Que 5  Write a program that takes your name and age as input and prints: 'My name is X and I am Y
#  years old.'
# name = input("enter your name :")
# age = input("enter your age :")

# print(f"My name is {name} and i am {age} years old now.")


#Que 6  Write a program to swap two variables using input from the user
# a = int(input("Enter first no.:"))
# b = int(input("Enter second no.:"))
# a = a + b
# b = a - b
# a = a - b
# print("after swapping: a =" ,a,"b =",b) 

# Que 7  Write a program to check whether a variable is mutable or immutable in Python (by attempting
#  modification).


# Que 8 Write a program to perform all arithmetic operations on two numbers
# a = int(input("Enter first no.:"))
# b = int(input("Enter second no.:"))
# print("Addition:",a+b)
# print("subtract:",a-b)
# print("Multiply:",a*b)
# print("divide:",a/b)
# print("Addition:",a+b)
# print("Modulus:",a%b)
# print("Power:",a**b)


# Que 9 . Write a program to check whether two numbers are equal using comparison operators
# a = int(input("Enter fiest number :"))
# b = int(input("Enter second number :"))
# if(a == b):
#     print("Numbers are equal")
# else:
#     print("Numbers are not equal")


# Que 10  Write a program to demonstrate bitwise operators (&, |, ^, <<, >>) on two numbers.
# a = 10
# b = 4

# print()


# Que 11  Write a program to check whether a number lies between 10 and 50 using logical operators.
# n = int(input("Enter your number :"))
# if(n >= 10 and n <= 50):
#     print("Your number is between 10 and 50")
# else:
#     print("Try again")


# Que 12 Write a program to check membership of an element in a list using 'in' and 'not in'


# Que 13 . Write a program to compare two objects using 'is' and 'is not'
# a = 10
# b = 10
# c = 20

# print ("a is b :", a is b)
# print("a is c :", a is c )

# print("a is not b :", a is not b)
# print("a is not c :", a is not c)


#Que 14  Write a program to check whether a number is positive, negative, or zero
# n = int(input("Enter your number :"))
# if(n > 0):
#     print("Number is positive")
# elif(n < 0):
#     print("Number is negative")
# else:
#     print("Number is zero")


# Que 15  Write a program to check whether a number is even or odd using if-else
# n = int(input("enter your number :"))
# if(n%2 == 0):
#     print("Number is Even")
# else:
#     print("Number is Odd")


# Que 16 Write a program to find the largest of three numbers using nested if-else
# a = int(input("Enter your first number :"))
# b = int(input("Enter your second number :"))
# c = int(input("Enter your third number :"))
# if(a > b and a > c):
#     print("a is greatest")
# elif(b > c):
#     print("b is greatest")
# else:
#     print("c is greatest") 



# Que 17  Write a program to print all numbers from 1 to 20 using a for loop
# i = 0
# for i in range(1, 21):
#     print(i)


# Que 18 Write a program to print the multiplication table of a given number using a while loop
# n = 5
# i = 0
# while i < 10:
#     i += 1
#     print(n*i)


# Que 19 Write a program to search an element in a list using for-else


# Que 20  Write a program to check whether a number is prime using a while-else


# Que 21  Write a program that prints numbers from 1 to 10 but skips 5 using continue
# i = 0
# while i < 10:
#     i += 1    
#     if(i == 5):
#         continue 
#     print(i)


# Que 22 Write a program that prints numbers from 1 to 10 but stops when it reaches 7 using break
# i = 0
# while i < 10:
#     i += 1    
#     if(i == 7):
#         break 
#     print(i)


# Que 23  Write a program that prints 'Hello' five times but does nothing when the loop counter is 3 (use
#  pass)
# for i in range(1, 6):  
#     if (i == 3):
#         pass
#     else:
#         print("Hello")


# Que 24  Write a program to create an iterator for a list and print all elements using next()







# Que 25 . Write a program to generate squares of numbers using a for loop with an iterator
# i = 0
# for i in range(1,11):
#     print("Square of number",i,"is",i**2) 