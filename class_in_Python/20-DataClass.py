from dataclasses import dataclass
#this class only save data and dosent have methods
@dataclass
class Employee:
    name: str
    family: str
    type: str
    salary: float
    age  :int


employee = Employee("soheila","nazeri",salary= 50000,age=37,type=1)
print(employee.name)
print(employee.family)
print(employee.salary)
print(employee.age)
print(employee.type )
