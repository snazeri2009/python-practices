#hasattr is a built-in function in Python that allows you to check 
# if an object has a particular attribute (e.g., method or variable).
#The function takes two arguments:
#an object, obj
#a string that specifies the name of the attribute, name
#If obj has an attribute named name, hasattr returns True. Otherwise, it returns False.

def make_something_speak(thing):
    if hasattr(thing, "speak"):  # if thins has speak method then 
        print("{} says {}".format(thing.name, thing.speak()))
    else: # if thins doesn't have speak method then
        print("{} can't speak".format(thing.name))

class Dog: #this class has speak method
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Woof!"

class Cat: #this class has speak method
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Meow!"

class Lamp:  #this class doesn't have speak method
    def __init__(self, name):
        self.name = name

dog = Dog("Fido")
cat = Cat("Tom")
lamp = Lamp("Light")

make_something_speak(dog)  # this line executed :print("{} says {}".format(thing.name, thing.speak()))
make_something_speak(cat) # this line executed :print("{} says {}".format(thing.name, thing.speak()))
make_something_speak(lamp) # this line executed :print("{} can't speak".format(thing.name))