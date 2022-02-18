class Shape:
    def shape(s):
        print("Shape area is 0")
        
class Square(Shape):
    def __init__(self, length):
        self.length = length
    
    def area(self):
        print("Shape area is", self.length**2)

p = Square(4)
p.area()



    