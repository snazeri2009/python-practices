

class Person:  # parennt or base class
    # this is the constructorوmagic Method for the Product class ,we create a magic Method : __name__
    def __init__(self, _name, _family, _type):
        self.name = _name
        self.family = _family
        self.type = _type
    # ===============================================   properties share with Person and children  =================================
    # name property

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value
    # ===============================================
    # family property

    @property
    def family(self):
        return self.__family

    @family.setter
    def family(self, value):
        self.__family = value
    # ===============================================
    # type property

    @property
    def type(self):  # getter
        return self.__type

    @type.setter
    def type(self, value):  #
        self.__type = value
    # ===============================================

    def get_information(self):
        return self.name + ' - ' + self.family + ' - ' + str(self.type)


class Teacher:
    Person  # child or subclass


class Student:
    Person  # child or subclass


class Employer:
    Person  # child or subclass


myPerson = Person(_name='human1', _family="human2", _type=1)
teacher1 = Person(_name='soheila', _family="nazeri", _type=2)
student1 = Person(_name='sima', _family="ahmadi", _type=3)
Employer1 = Person(_name='sara', _family="mohammadi", _type=4)

print(myPerson.get_information(), isinstance(myPerson, Person))
print(teacher1.get_information(), isinstance(teacher1, Person))
print(student1.get_information(), isinstance(student1, Person))
print(Employer1.get_information(), isinstance(Employer1, Person))

# isinstance(Employer1,Person) Determines whether it exists or inherits from the desired class
# returns true because teacher inherits from the desired class
print(issubclass(Teacher, object))
# returns true because student inherits from the desired class
print(issubclass(Student, Person))
# returns true because employer inherits from the desired class
print(issubclass(Employer, object))
# returns true because employer inherits from the desired class
print(issubclass(Employer, Person))
