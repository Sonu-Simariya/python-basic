# pyramid
a=int(input("enter number "))
for i in range(0,a):
    for k in range(a-i):
        print(" ",end=" ")
    for l in range(i):
        print(l+1,end=" ")
    for j in range(i+1):
        print(i-j+1,end=" ")
    print()

# reverse pyramid
a=int(input("enter number: "))
for i in range(0,a):
    for k in range(i):
        print(" ",end=" ")
    for j in range(a-i-1):
        print(j+1,end=" ")
    for l in range(a-i):
        print(a-l-i,end=" ")
    print("")

    