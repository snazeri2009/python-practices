# there are two ways to create a method
# instance_method
# class Method

# create a new class
class Point:
    # this is the attribute that will be added to the class
    # all of the objects in this class can be used to this attribute
    default_z = 200
    # this is the constructor for the Point class

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # this is the instance method for the Point class
    # this means this method will be called when the class is created and object is created
    #instance_method = Point.instance_method

    def draw(self):
        print("drawing")
        print(" x is  ", self.x)
        print(" y ia  ", self.y)
        print(f"x is {self.x}, y is {self.x}")

    # this is factory function or factory method
    @classmethod
    def zero(Point):  # class
        return Point(0, 0)   # refrence __init__
        # return Point(0,0,0)   # an Error show


class square:
    default_z = 200
    # this is the constructor for the square class

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    # this is factory function or factory method
    @classmethod
    def zero(square):  # class
        return square(0, 0, 0, 0)   # refrence __init__
        # return square(0,0,0)   # an Error show

    @classmethod
    def equalvalues(square):  # class
        return square(10, 10, 10, 10)   # refrence __init__


# this method creates a new object from a square and set values 0,0 and returns a new instance
p2 = square.zero()
print(p2.x1, p2.y1, p2.x2, p2.y2)

# create a new object from a square and set values 10,10,10,10 and return a new instance
p2 = square.equalvalues()
print(p2.x1, p2.y1, p2.x2, p2.y2)


p1 = Point.zero()  # this method creates a new object from a point and set values 0,0 and returns a new instance
print(p1.x, p1.y)
#
