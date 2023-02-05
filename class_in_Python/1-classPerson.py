#create a new class
class Person:
    #this is the constructor for the person class
    def __init__(self, name,family ,age):
        self.name = name
        self.age=age
        self.family = family

#create the object  for the person class
#create a new   instance    
p1 = Person("Amir", "Ahmadi", 30)

#create the object  for the person class
#create a new   instance    
p2 = Person("soheila", "Nazeri", 37)

#print value of family,age,name of p1
print(p1.name)
print(p1.age)
print(p1.family)

#print value of family,age,name of p2
print(p2.name)
print(p2.age)
print(p2.family)

# print check(p1.family) values equal to    p2.family ,...
print(p1.name == p2.name)
print(p1.age == p2.age)
print(p1.family == p2.family)

# to Get Type of Person
print(type(p1))
# to check if type of Person is Person
print(isinstance(p1,Person)) # true because type of Person is   person
print(isinstance(p1,object)) # true because type of Person is   object . object is parenth of all objects
