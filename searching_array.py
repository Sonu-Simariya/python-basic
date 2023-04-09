import array as arr
aj=arr.array('i',[])
ar=int(input("enter number of value in array"))
for i in range(ar):
    a=int(input("enter value"))
    aj.append(a)
print(aj)
val=int(input("enter value you want to search"))
k=0
for e in aj:
    if e==val:
        print(k)
        break
    k+=1 
