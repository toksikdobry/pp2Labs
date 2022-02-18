class Shape:
    def shape(s):
        print("Shape area is 0")
        
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width  = width

    def area(self):
        print("Shape area is", self.length * self.width)

p = Rectangle(4, 5)
p.area()