class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        print(f"{self.name} is working.")


class Manager(Employee):
    def __init__(self, name, salary, subordinates):
        super().__init__(name, salary)
        self.subordinates = subordinates

    def work(self):
        print(f"{self.name} is managing.")
        for subordinate in self.subordinates:
            subordinate.work()


class Intern(Employee):
    def work(self):
        print(f"{self.name} is interning.")


def work_all(employees):
    for employee in employees:
        employee.work()


employees = [
    Employee("John Doe", 50000),
    Manager("Jane Doe", 75000, [Employee(
        "Jim Smith", 55000), Intern("Tommy Lee", 0)]),
    Intern("Liza Martinez", 0)
]

# print(isinstance(employees,Employee))
print(employees[1])
work_all(employees)
