#create a new class
class Point:
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

#print value of x,y from the point
print(p1.x,p1.y)

#print value of x,y from the point
print("x in p2 :" ,p2.x)
print("y in p2 :",p2.y)

# to Get Type of Point
print("type of p1 is :" ,type(p1))
# to check if type of Point is Point
print("isinstance :" ,isinstance(p1,Point)) # true because type of Point is   Point
print("isinstance :" ,isinstance(p1,object)) # true because type of Point is   object . object is parenth of all objects
#call the method in the Point class
p1.draw()

#add attributes to the point class outside of the class
p1.z=100
print(p1.z,p1.z+100)
p1.w=200
print(p1.z,p1.w)

