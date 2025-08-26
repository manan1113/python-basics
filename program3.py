# swap two numbers without using a third variable(using arithmetic operators)
a = int(input("enter no.:"))
b = int(input("enter no.:"))
a = a+b
b = a-b
a = a-b
print("after swapping:a =",a,"b =",b)
