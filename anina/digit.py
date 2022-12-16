z=[]
n=int(input("enter the number of element in list:"))
for x in range (0,n):
    elem=input("enter element"+str(x+1)+":")
    z.append(elem)
    max1=len(z[0])
    temp=z[0]
    for i in z:
        if(len(i)>max1):
            max1=len(i)
            temp=i
print("the word with the longest is:",max1)
print(temp)