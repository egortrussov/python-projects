import math

class Point():
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        self.coords = (self.x, self.y)
    
    def move(self, x, y):
        self.x += x 
        self.y += y 
    
    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)
    
    def __add__(self, p):
        return Point(self.x + p.x, self.y + p.y)
    
    def __sub__(self, p):
        return Point(self.x - p.x, self.y +- p.y)
    
    def __mul__(self, p):
        return self.x * p.x + self.y * p.y
    
    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'
    
    def __eq__(self, p):
        return self.length() == p.length()
    

p1 = Point(0, 10)
p2 = Point(10, 0)
p3 = Point(5, 2)
p4 = Point(0, 3)

p5 = p1 + p2
p6 = p3 * p2
print(p5.x, p5.y)
print(str(p5))
print(p1 == p2)