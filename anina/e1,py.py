n = int(input("Enter the 1st list elements : "))
x=[]
for i in range(0, n):
    i = input()
    x.append(i)
a=len(x)
print(a)
m=int(input("enter the number of elements:"))
y=[]
for i in range(0, m):
    i = input()
    y.append(i)
b=len(y)
if (a==b):
    print("list is same length")
else:
    print("not a same length")
if(sum(x)==sum(y)):
    print("list sum to same value")
else:
    print("list sum to not same value")
print("value occur in both:")
for i in x:
    if i in y:
        print(i)