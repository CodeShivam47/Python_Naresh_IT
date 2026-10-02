# 1. =->
# class  employee:
#     def __init__ (self, name, salary):
#         self.name = name
#         self.salary = salary
#     def monthly_pay(self):
#         return self.salary /12
# emp1 = employee("Chhaya", 12000)
# emp2 = employee("Shivam", 14000)

# print(emp1.name,"earns INR", f"{emp1.monthly_pay() : ,.2f}", "per months")
# print(emp2.name,"earns INR", f"{emp2.monthly_pay():,.2f}", "Per months ")



# 2. ->
# class BankCustomer:
#     def __init__(self, name , city):
#         self.name = name 
#         self.city = city
# c1 = BankCustomer("Ananya", "Hyderabad")
# c2 = BankCustomer("Raghav","Maihar")

# print(type(c1))
# print(c1.name,"", c1.city)
# print(c2.name,"",c2.city)


#3. =>
# class SupportTicket:
#     def __init__(self, ticket_id, issue):
#         self.ticket_id = ticket_id
#         self.issue = issue
#     def close(self):
#         self.status = "clossed"
#     def summary(self):
#         return f"Ticket {self.ticket_id}: {self.issue} [{self.status}]"
# t1 = SupportTicket(101, "Card not delevered")
# print(t1.summary())
# t1.close()
# print(t1.summary())

# 4. => 
# class Patient:
#     def __init__(self, name, age):
#         self.name = name 
#         self.age = age
#     def is_senior(self):
#         return self.age>= 60
# patient1 = Patient("Ravi", 56)
# patient2 = Patient("Satya", 90)

# print(f"name: => {patient1.name} age : => {patient1.age}")
# print(f"name: => {patient2.name} age : => {patient2.age}")


# 5. =>
# class SavingAccounts:
#     interest_rate = 0.04

#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance
#     def yearly_interest(self):
#         return self.balance * SavingAccounts.interest_rate
# a1 = SavingAccounts("Manya", 50000)
# a2 = SavingAccounts("Neha", 120000)

# print(f"manya interest : INR {a1.yearly_interest():,.2f}")
# print(f"neha ionterest : INR {a2.yearly_interest():,.2f}")
    
# 6. =>
# class Bill:
#     gst_rate = 0.18

#     def __init__(self, amount):
#         self.amount = amount

#     def total_woth_gst(self):
#         return self.amount *(1 + Bill.gst_rate)
# b1 = Bill(1000)
# b2 = Bill(2500)

# print(f"Bill 1 total INR :{b1.total_woth_gst():,.2f}")
# Bill_gst_rate = 0.12
# print(f"Bill 2 total INR :{b2.total_woth_gst():,.2f}")


# 3 @ classmethods.....

# 1. =>
# class Employee:
#     compary = " techCorp"
#     def __init__(self, name, salary):
#         self.name = name 
#         self.salary = salary
#     @classmethod
#     def from_record(cls, record):
#         name, salary = record.split(",") # aplit( )from day 8
#         return cls(name, float(salary)) # cls means this class
# emp = Employee.from_record("Anita Deshai, 860000")
# print(emp.name, "Joined", Employee.compary)
# print(f"salary : INR {emp.salary:,.2f}")
        



#2 . =>
# class SafeBank:
#     @staticmethod
#     def is_valid_ifsc(code):
#         return len(code) == 11
#     # => Bank ifsc code only 11 Character
# print(SafeBank.is_valid_ifsc("SAFE0000000"))
# print(SafeBank.is_valid_ifsc("SAFEBANK"))


# 3 =>
# class Product:
#     store = "NeoMart"

#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

#     @classmethod
#     def from_string(cls, text):
#         name, price = text.split(",")
#         return cls(name, float(price))

#     @staticmethod
#     def is_valid_price(price):
#         return price > 0

# p = Product.from_string("Basmati Rice 5kg,450")
# print(p.store, "-", p.name, "- INR", f"{p.price:,.2f}")
# print("Valid price?", Product.is_valid_price(p.price))





# 4. =>
# class ReportFile:
#     def __init__(self, name):
#         self.name = name
#         print("Opened :", self.name)
#     def __del__(self):
#         print("Clean Up:", self.name)
# report = ReportFile("Daily sale Report...")
# print("....Working with the reports....")
# del report
# print("report Continue..")


# 5. ->
# class Order:
#     def __init__(self, order_id, amount):
#         self.order_id = order_id
#         self.amount = amount

# amounts = [1250.50, 890.00, 2340.75, 560.25]   # arrived from a sales file
# orders = []
# order_id = 101
# for amt in amounts:
#     orders.append(Order(order_id, amt))        # one object per order
#     order_id += 1

# total = 0
# for order in orders:           
#     total += order.amount

# print("Orders stored:", len(orders))
# print(f"Total sales : INR {total:,.2f}")
# print("First order :", orders[0].order_id, "for INR", orders[0].amount)



# 3. ->
# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance

# accounts = [BankAccount("Priya Sharma", 5000),
#             BankAccount("Rahul Verma", 12000),
#             BankAccount("Anita Desai", 800)]

# richest = accounts[0]
# for acct in accounts:
#     if acct.balance > richest.balance:
#         richest = acct

# print("Highest balance:", richest.owner, f"INR {richest.balance:,.2f}")




# 4. ->
# class Trainer :
#     def __init__(self, name, annual_salary):
#         self.name = name
#         self.annual_salary = annual_salary
#     def payslip_line(self):
#         monthly = self.annual_salary / 12
#         return f"{self.name} | monthly INR : {monthly:,.2f}"
# t1 = Trainer("Priya Sharma", 500000)
# t2 = Trainer("Shivam Sharma", 10000)

# print(t1.payslip_line())
# print(t2.payslip_line())


# AP2 ->
