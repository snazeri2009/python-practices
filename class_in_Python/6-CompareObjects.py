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

    def __eq__(self, other):
        return self.x1 == other.x1 and self.y1 == other.y1 and self.x2 == other.x2 and self.y2 == other.y2

    def __gt__(self, other):
        return self.x1 > other.x1 and self.y1 > other.y1 and self.x2 > other.x2 and self.y2 > other.y2

    def __lt__(self, other):
        return self.x1 < other.x1 and self.y1 < other.y1 and self.x2 < other.x2 and self.y2 < other.y2


# __str__
square1 = square(10, 10, 20, 20)
square2 = square(10, 10, 20, 20)
print(square1, "*", square2)
print("eq :", square1 == square2)
print('===================')

square3 = square(30, 30, 40, 50)
square4 = square(10, 10, 20, 20)
print(square3, "*", square4)
print("gt :", square3 > square4)
print('===================')

square5 = square(10, 10, 20, 20)
square6 = square(30, 30, 40, 50)
print(square5, "*", square6)
print("lt : ", square5 > square6)
print('===================')
