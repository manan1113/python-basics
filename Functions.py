# Functions in python 
# A function is a block of code that performs a specific task :
# It helps in code reusebility :

# def function_name(parameters):
    # fuction body 
    # fuction value 

# def greet(name):
#     return f"hello ,{name}!"
# print(greet("Nikhil"))

# nums=[10,20,30]
# print(len(nums))
# print(max(nums))
# print(min(nums))
# print(sum(nums))

# def square(x):
#     return x*x
# print(square(5)) # calling out functions 

# def add(a,b):
#     return a+b
# res=add(10,20)
# print("the sum is ",res)

# a = int(input("Enter no."))
# b = int(input("Enter no."))
# def add(a,b):
#     return a+b
# sum=add(a,b)
# print("Sum is :",sum)

# passing arugments 
# def greet(name="guest"):
#     print(f"hello {name}!")
# greet()
# greet("alice")
# greet("spiderman")    

# Recursion 
# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     return n * factorial(n - 1)
# print("factorial of 5 is ",factorial(5) )
 
# yield : yield is like a return , but instead of returning once, it returns a sequence of values one by one.
def simple_generator():
    yield 1
    yield 2
    yield 3
for value in simple_generator():
    print(value)









