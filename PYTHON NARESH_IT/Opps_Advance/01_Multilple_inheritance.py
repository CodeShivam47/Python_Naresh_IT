class Employee:
    def __init__(self, name , salary):
        self.name = name
        self.salary = salary
class Maneger(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)   # parent sets name and salary
        self.team_size = team_size # then we add what is new


m = Maneger("Priya Sharma", 800000, 8)
print(m.name, "manegar" , m.team_size, "People")
print(f"Salary: INR {m.salary:,.2f}")
