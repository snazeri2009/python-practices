from collections import namedtuple

# Define a named tuple class
Employee = namedtuple('Employee', ['name', 'age', 'salary'])

# Create an instance of the named tuple
e = Employee('soheila nazeri', 37, 50000)

# Access elements of the named tuple
print(e.name)  # prints: John Doe
print(e.age)   # prints: 30
print(e.salary)  # prints: 50000

e.name=10  #this line shows the error message because named tuple can not be changed