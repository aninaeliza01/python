class rectangle():
    def _init_(self):
        self._length = int(input("Enter the Length:"))
        self._breadth = int(input("Enter the Breadth:"))
        self.area = self._length * self._breadth
    def greaterThan(self,rectangle):
        if self.area < rectangle.area:
            print("Area of Object 1 is Greater")
        else:
            print("Area of Object 2 is Greater")

print("Object 1:-")
r1 = rectangle()
print("Object 2:-")
r2 = rectangle()
print("Comparing Objects:-")
r2.greaterThan(r1)