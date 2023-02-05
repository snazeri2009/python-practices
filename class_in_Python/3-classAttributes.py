#create a new class
class Point:
    # this is the attribute that will be added to the class
    #all of the objects in this class can be used to this attribute
    default_z = 200
    #this is the constructor for the Point class
    def __init__(self, x,y):
        self.x = x
        self.y=y
        
    def draw(self) :
        print ("drawing")
        print (" x is  ",self.x)
        print (" y ia  ",self.y)
        print (f"x is {self.x}, y is {self.x}")

#create the object  for the point class
#create a new   instance    
p1 = Point(10,20)
#create the object  for the point class
#create a new   instance    
p2 = Point(30,40)

#with create the object of the point class
print(p1.default_z)
print(p2.default_z)

#without create the object of the point class only use the point class
print(Point.default_z)

#change the default value of the point class
p1.default_z = 100
print(p1.default_z)

#change the default value of the point class with class
Point.default_z=300
p3=Point(100,200)
p4=Point(100,200)
print(p3.default_z)
print(p4.default_z)
