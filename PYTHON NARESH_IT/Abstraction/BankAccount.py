class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def yearly_interest(self):
        return self.balance*0.0   # current accounts earn nothing
class SavingsAccount(Account):
    def yearly_interest(self):
        return self.balance * 0.04   # OVERRIDES the base rule

class FixedDepositAccount(Account):
    def yearly_interest(self):
        return self.balance * 0.071

accounts = [SavingsAccount("Priya Sharma", 50000),
            FixedDepositAccount("Rahul Verma", 200000),
            Account("Anita Desai", 15000)]
total_payounts = 0
for acct in accounts:
    interest = acct.yearly_interest()
    total_payounts += interest
    #print(f"{acct.owner:12} | INR | {interest:,.2f}")
#print(f"total interest payouts : INR  {total_payounts:,.2f}")


# Medicare staff Payrolls Payments
from abc import ABC,abstractmethod
class HospitalStaf(ABC):
    def __init__(self,name):    # contract: every staff type must price a day
         self.name = name

    @abstractmethod
    def daily_wage(self):
        pass

class Nurse(HospitalStaf):
    def daily_wage(self):
        return 12 * 300       # 12-hour shift at INR 300/hour

class Surgeon(HospitalStaf):
    def daily_wage(self):
        return 1500           # flat daily rate

staff = [Nurse("Priya sharma"), Surgeon("Shibbu Pandit")]
payrolls = 0
for member in staff:
    wage = member.daily_wage()
    payrolls += wage
   # print(f"{member.name:12} INR {wage:,.2f}")
#print(f"Total daily payrolls INR: {payrolls:,.2f}")





class Product:
    def __init__(self, name, price, stock):
        self.name, self.price, self._stock = name, price, stock

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, value):
        if value < 0:
            print(f"Rejected: {self.name} stock cannot be negative")
        else:
            self._stock = value

    def final_price(self):
        return self.price             # base rule: price as-is

class Electronics(Product):
    def final_price(self):
        return self.price * 1.18      # 18% GST

class Luxury(Product):
    def final_price(self):
        return self.price * 1.28      # NEW category: 28% GST

inventory = [Electronics("Headphones", 2500, 10),
             Luxury("Designer Watch", 12000, 3),
             Product("Notebook", 60, 200)]
ordered_qty = {"Headphones": 2, "Designer Watch": 1, "Notebook": 10}

print("NeoMart Invoice")
print("-" * 48)
grand_total = 0
for item in inventory:                # polymorphism: one loop, three tax rules
    qty = ordered_qty[item.name]
    line_total = item.final_price() * qty
    grand_total += line_total
    print(f"{item.name:15} x{qty:2}  @ INR {item.final_price():>9,.2f}"
          f"  = INR {line_total:,.2f}")
print("-" * 48)
print(f"{'GRAND TOTAL':22} INR {grand_total:,.2f}")

print()
for item in inventory:                # fulfilment through the guarded setter
    item.stock = item.stock - ordered_qty[item.name]
    print(f"{item.name:15} remaining stock: {item.stock}")
    