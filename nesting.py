# nested loops 
for i in range(1,4):
    for j in range(1,4):
        print(i*j,end=" ")
    print()

# star program 
rows = 5
for i in range(1,rows+1):
    for j in range(i):
        print("*",end=" ")
    print()

rows = 5
for i in range(1,rows+1):
    for j in range(i):
        print(i,end=" ")
    print()

rows = 5
num = 1
for i in range(1,rows+1):
    for j in range(i):
        print(num,end=" ")
        num+=1
    print()

rows = 10
for i in range(rows,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()

n = int(input("Enter no:"))
for i in range(1,n+1):
    for j in range(n-i):
        print(" ", end="")
    for k in range(i):
        print("*",end="")
    print()

n = int(input("Enter no:"))
for i in range(1,n+1):
    for j in range(n-i):
        print(" ", end="")
    for k in range(i):
        print("*",end=" ")
    print()





