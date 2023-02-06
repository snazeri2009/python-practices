class square:
    # this is the constructor for the square class
    # we create a magic Method : __name__
    # this is a magic method
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    # i changed default __str__ magic method
    # please comment this and then run and see output
    # then remove commented lines and run and see output

    def __str__(self):
        return (f"{self.x1}, {self.y1}, {self.x2},{self.y2}")


# __str__
square1 = square(10, 10, 20, 20)
print(square1)   # __Str__  default
print(square1.__str__)   # __Str__  default
# when user this code return this
# <__main__.square object at 0x0000022E77876310>
# main is name of the module
# square is name of the square class
# object at 0x0000022E77876310> address of the square object
