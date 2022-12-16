class el1():
    def _init_(self,a):
        self.a=int(input("Enter the Element to class A:"))
class el2(el1):
    def __init__(self,b,a):
        self.b = b
        el1.__init__(self, a)
        self.b = int(input("Enter the Element to class B:"))

class el3(el2):
    def __init__(self, c, b, a):
        self.c = c
        el2.__init__(self,b,a)
        self.c = int(input("Enter the Element to class C:"))

a=el3()
if a.a > a.b and a.b > a.c:
    print("Element of Class A is Greatest:",a.a)
elif a.b > a.a and a.a > a.c:
    print("Element of Class B is Greatest:", a.b)
else:
    print("Element of Class C is Greatest:", a.c)