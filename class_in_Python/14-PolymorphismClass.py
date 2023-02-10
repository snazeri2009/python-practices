# polymorphic with abstract class methods and abstract clss
from abc import ABC, abstractclassmethod


class Animal:
    def __init__(self, name):
        self.name = name

    @abstractclassmethod
    def speak(self):   # this method uses for all of object
        pass


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


class bird(Animal):
    def speak(self):
        return "jick-jick!"


# this is polymorphic with abstract class methods and abstract class
def make_animal_speak(animal):
    print("{} says {}".format(animal.name, animal.speak()))


def animal_speak(control):  # this is polymorphic with abstract class methods and abstract class
    print(control.speak())

# this is polymorphic with abstract class methods and abstract class
# this method get list of objects


def lst_animal_speak(controls):
    for control in controls:
        print(control.speak())


mydog = Dog("Fido")
mycat = Cat("Whiskers")
mybird = bird("rolly")
print("========================")
animal_speak(mydog)
animal_speak(mycat)
animal_speak(mybird)
print("========================")
make_animal_speak(mydog)
make_animal_speak(mycat)
make_animal_speak(mybird)
print("========================")
lst_animal_speak([mybird, mydog, mycat])
print("========================")
