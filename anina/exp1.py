x=int(input("enter the starting year:"))
y=int(input("enter the end year:"))
print("leap years")
for i in range(x,y):
    if(((i%400==0)and(i%100==0))or((i%100!=0)and(i%4==0))):
        print(i)