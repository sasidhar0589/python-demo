class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y
class Circle:
    
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        from math import pi
        return  pi* self.radius * self.radius
class Square:
    
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side * self.side
class Triangle:
    
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height

shapes = [Shape(10, 20), Circle(10), Square(10), Triangle(10, 20)]
# shape = Shape(10, 20)
# print(shape.area())
# circle = Circle(10)
# square = Square(10)
# triangle = Triangle(10, 20)
for shape in shapes:
    print(shape.area())
    
stack = []
stack.append(10)
stack.append(20)
stack.append(5)
stack.sort(reverse=True)
print(stack)


stack.pop()
stack.pop()
stack.pop()
stack.pop()
print(stack)