# bad implementation of ocp 
class AreaCalculator:
    def calculate_area(self, shapes):
        area = 0
        # we would have to modify this in order to add mroe shapes 
        for shape in shapes:
            if shape.type == "rectangle":
                area += shape.width * shape.height
            elif shape.type == "square":
                area += shape.length ** 2

        return area
    
# proper application of ocp
class Shape:
    def area(self):
        print(f"This is the area of this shape")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2
    
class Circle(Shape):
    def __init__(self, radius, pi=3.142):
        self.radius = radius
        self.pi = pi

    def area(self):
        return self.pi * self.radius ** 2
    
class Triangle(Shape):
    pass
    
class NewAreaCalculator:
    def total_area(shapes):
        # print (shapes)
        areas = [] 
        total = 0
        for shape in shapes:
            # print (shape.area())
            areas.append(shape.area())
            total += shape.area()
        return areas
        
        


rectangle = Rectangle(5,10)
square = Square(10)
circle = Circle(4)

shapes = [rectangle, square, circle]

print(NewAreaCalculator.total_area(shapes)) 

for shape in shapes:
    print (shape)