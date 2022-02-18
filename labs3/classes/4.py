class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print("Point (x = ",self.x," and y = ",self.y,")", sep = "")

    def move(self, direct):
        def __init__(self, direct):
            self.direct = direct
        if(direct == "Left"): self.x -= 1
        if(direct == "Right"): self.x += 1
        if(direct == "Up"): self.y += 1
        if(direct == "Down"): self.y -= 1

    def dist(self, point):
        def __init__(self, point):
            self.point = point
        distance = ((self.x - point.x)**2 + (self.y - point.y)**2)**0.5
        print("Distance between points: ",distance)
            
p1 = Point(1, 1)
p2 = Point(2, 2)
print(p1.dist(p2))