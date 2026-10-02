# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#     def bonus(self):
#         return self.salary * 0.05  # stardard 55 bonus
# class SalesExecutive(Employee):
#     def bonus(self):
#         return self.salary * 0.05 + 25000
# e = Employee("Shivam sharma", 500000)
# print(f"Rahul bonus: INR {e.bonus():,.2f}")


# 2. =>
class Report:
    def header(self):
        return "NeoMart Sales Report"

class RegionalReport(Report):
    def header(self):
        base = super().header()            # reuse the parent's text
        return base + " - South Region"

print(Report().header())
print(RegionalReport().header())



