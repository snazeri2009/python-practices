# In Python, a data class is a class designed to store data. It is typically used to store data structures t
# hat can be represented as a collection of attributes. A data class is typically simpler
#  and more lightweight compared to a regular class, as it does not include any logic or methods
#  beyond those necessary to store and manage its data.


from dataclasses import dataclass
# this class only save data and dosent have methods


@dataclass
class Employee:
    name: str
    family: str
    type: str
    salary: float
    age: int


employee = Employee("soheila", "nazeri", salary=50000, age=37, type=1)
print("name is :", employee.name)
print("family is :", employee.family)
print("salary is :", employee.salary)
print("age is :", employee.age)
print("type is :", employee.type)
