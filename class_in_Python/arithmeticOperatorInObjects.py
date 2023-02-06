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
   # add one object to another object

    def __add__(self, other):
        return square(self.x1 + other.x1, self.y1 + other.y1, self.x2 + other.x2, self.y2 + other.y2)
    # subtract one object to another object

    def __sub__(self, other):
        return square(self.x1 - other.x1, self.y1 - other.y1, self.x2 - other.x2, self.y2 - other.y2)

    def __mul__(self, other):
        return square(self.x1 * other.x1, self.y1 * other.y1, self.x2 * other.x2, self.y2 * other.y2)


# __str__
square1 = square(0, 80, 20, 100)
square2 = square(25, 10, 75, 20)
print('===================')
print("+ :", square1 + square2)
print("- :", square1 - square2)
print("* :", square1 * square2)
print('===================')
