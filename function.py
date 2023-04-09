a=int(input("entr number"))
# b=int(input("enter numer"))
def average(a):
    for i in range(a):
        for j in range(a-i):
            print(" ",end=" ")
        for k in range(i):
            print(k+1,end=" ")
        for l in range(i-1):
            print(a-i-j,end=" ")
        print("")
def aveg(a):
    for i in range(a):
        for m in range(i):
            print(" ",end=" ")
        for j in range(a-i-1):
            print(j+1,end=" ")
        for l in range(a-i):
            print(a-i-l,end=" ")
        print("")
average(a)
aveg(a)