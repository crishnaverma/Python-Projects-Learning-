class Shape:
    def area (self):
        print("Area of the shape")

class Cricle(Shape):
    def __init__(self,radius):
        self.radius = radius
    
    def area (self):
        print(f"Area of circle {3.14 * self.radius**2}")

class Rectangle(Shape):
    def __init__(self,length,breath):
        self.length = length
        self.breath = breath
    
    def area (self):
        print(f"Area of rectangle {2 * (self.length + self.breath)}")

class Triangle(Shape):
    def __init__(self,base,height):
        self.base = base
        self.height = height
    
    def area (self):
        print(f"Area of rectangle {0.5* (self.base + self.height)}")


c = Cricle(5)
r = Rectangle(4,6)
t = Triangle(2,4)

c.area()
r.area()
t.area()
