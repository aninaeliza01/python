a=int(input("Enter the number of string:"))
print("Enter the string:")
li=[]
count=0
for i in range(0,a):
    el=input()
    li.append(el)
print(li)
for i in li:
    for j in i:
        if(j=='a'):
            count=count+1
print(count)