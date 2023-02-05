#create a new class
class Point:
    # this is the attribute that will be added to the class
    #all of the objects in this class can be used to this attribute
    default_z = 200
    #this is the constructor for the Point class
    def __init__(self, x,y):
        self.x = x
        self.y=y
    
    #this is the instance method for the Point class    
    #this means this method will be called when the class is created and object is created
    def draw(self) :
        print ("drawing")
        print (" x is  ",self.x)
        print (" y ia  ",self.y)
        print (f"x is {self.x}, y is {self.x}")

Factory


