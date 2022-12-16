x=[10,11,5]
y=[2,5,8]
a=len(x)
b=len(y)
if a==b:
    print("list is same length")
else:
    print("not a same length")
if(sum(x)==sum(y)):
    print("list sum to same value")
else:
    print("list sum to not same value")
print("value occur in both")
for i in x:
    if i in y:
        print(i)