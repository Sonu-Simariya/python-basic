def ss1(a):
    c=0
    for i in range(a+1):
        for j in range(a-i):
            print(" ",end=" ")
        for k in range(i+1):
            print(chr(65+c),end=" ")
            c+=1
        for l in range(i):
            print(chr(65+c),end=" ")
        print(" ")
    for i in range(a-1,-1,-1):
        for j in range(a-i):
            print(" ",end=" ")
        for k in range(i+1):
            print(i,end=" ")
        for l in range(i):
            print(i,end=" ")
        print(" ")
ss1(int(input("enter value")))