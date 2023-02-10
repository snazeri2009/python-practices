# polymorphic with abstract class methods and abstract clss
from abc import ABC, abstractclassmethod


class Shape:
    def __init__(self, name):
        self.name = name

    @abstractclassmethod
    def area(self):  # this method uses for all of object
        pass


class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


# this is polymorphic with abstract class methods and abstract class
def calculate_area(shape):
    print("The area of the {} is {}".format(shape.name, shape.area()))


rect = Rectangle("Rectangle", 10, 5)
circ = Circle("Circle", 2)

calculate_area(rect)
calculate_area(circ)
