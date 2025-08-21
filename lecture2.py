# conditional statements
a=int(input("enter your age:"))
if a>18:
    print("elligible to vote")
elif(a==18):
    print("wait for some time")  
else:
    print("try next time")      

marks=int(input("enter marks :"))
if(marks>=90 and marks<=100):
    grade="a+"
elif(marks>=75 and marks<90):  
    grade="a"
elif(marks>=60 and marks<75):
    grade="b"
elif(marks>=40 and marks<60):
    grade="c"
elif(marks>=0 and marks<40):
    grade = "fail"
else:
    grade = "invalid"
print("your grade =",grade)

# Taking input from the user to check if a no. is odd aur even
num = int(input("enter no."))
if(num % 2 == 0):
    print("number is even")
else:
    print("number is odd")





