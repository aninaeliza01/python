class rectangle:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
       return (self.l*self.b)
    def peri(self):
        return (2*(self.l+self.b))
l=int(input("enter the length:"))
b=int(input("enter the breadth:"))
o=rectangle(l,b)
x=o.area()
y=o.peri()
print("area is ",x)
print("preimeter is",y)
l1=int(input("enter the lenght:"))
b1=int(input("enter the breadth:"))
o1=rectangle(l1,b1)
z=o1.area()
z1=o1.peri()
print("area is ",z)
print("perimeter is ",z1)
if(x>z):
    print("frist rectangele is greater than 2")
else:
    print("second rect is greater")