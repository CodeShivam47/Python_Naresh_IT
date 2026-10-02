# multilevel inheritance
class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person): # level 2
     def __init__(self, name, emp_id):
         super().__init__(name)
         self.emp_id = emp_id

class Manegar(Employee): # level 3
    def __init__(self, name, emp_id, team_size):
        super().__init__(name, emp_id)
        self.team_size = team_size

M = Manegar("Anita Deshai",101,12)
print(f"{M.name} | {M.emp_id} | Team Size {M.team_size}")
print(isinstance(M,Person))    # Manegar is also a persons