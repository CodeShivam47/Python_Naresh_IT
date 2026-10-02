#   Single level inheritance
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def details(self):
        return f"{self.name} | INR {self.salary:,.2f}"

class Manager(Employee):              # Manager IS-A Employee
    def approve_leave(self, emp_name):
        return f"{self.name} approved leave for {emp_name}"

boss = Manager("Anita Desai", 1500000)
print(boss.details())                 # inherited from Employee
print(boss.approve_leave("Rahul Verma"))   # Manager's own method


    
