class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def compute_area(self):
        return self.length * self.width

# Testing the Rectangle class
rectangle = Rectangle(5, 10)
print("The area of the rectangle is: ", rectangle.compute_area())