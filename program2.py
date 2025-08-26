# write a program to check whether a given number is even or odd using the modulus operator 
num = int(input("Enter no.:"))
rem = num % 2
if(rem==0):
    print("even")
else:
    print("odd")
    