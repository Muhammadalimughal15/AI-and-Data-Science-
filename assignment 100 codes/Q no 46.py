import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def compute_area(self):
        return math.pi * (self.radius ** 2)

# Testing the Circle class
circle = Circle(5)
print("The area of the circle is: ", circle.compute_area())