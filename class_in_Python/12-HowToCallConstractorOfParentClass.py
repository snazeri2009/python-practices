
class Person:  # parennt or base class
    # this is the constructorوmagic Method for the Product class ,we create a magic Method : __name__
    def __init__(self, _name=None, _family=None, _type=None):
        print('in person class')
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


class Teacher(Person):      # child or subclass

    def __init__(self, _age=None):
        super().__init__(_type=1)
        print('in teacher Teacher')
        self.age = _age


class Student(Person):  # child or subclass

    def __init__(self, _age=None):
        super().__init__(_family="nazeri", _type=2)
        print('in student  class')
        self.age = _age


class Employer(Person):  # child or subclass

    def __init__(self, _age=None):
        super().__init__(_name="soheila", _type=3)
        print("in  Employee class ")
        self.age = _age


# when creating an object from teacher or student or employee if
# you don't want to see an error message for family ,name,_type you must to use supper()
# becase name,family,_type are in the person class (parent)
# and you have constructor in Teacher,student,employer and when you create an object student constructor is called
# and person constructor is not called


myTeacher = Teacher(10)
myEmployer = Employer()
myStudent = Student(20)

print("Age is :", myTeacher.age, "Name is :", myStudent.name)
print("Age is :", myEmployer.age, "Name is :", myEmployer.name)
print("Age is :", myStudent.age, "Name is :", myStudent.name)
