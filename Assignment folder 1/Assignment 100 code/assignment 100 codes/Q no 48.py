# python
class Shape:
    def __init__(self):
        pass

    def area(self):
        print("The area of the shape is 0 by default.")

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        print("The area of the square is: ", self.length ** 2)

# Testing the Shape class
shape = Shape()
shape.area()

# Testing the Square class
square = Square(5)
square.area()