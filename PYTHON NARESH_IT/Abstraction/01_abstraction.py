# Abstraction With Abc
from abc import ABC, abstractmethod

class PaymentGetway(ABC):  # abstract base class: a contract
    @abstractmethod
    def pay(self, amount):
        pass

class UPIGateway(PaymentGetway):  # fulfils the contrac
    def pay(self, amount):
        return f"UPI payment of INR {amount:,.2f} successful"

gateway = UPIGateway() 
#print(gateway.pay(1499))



# 2. Project(1) =>
class product:
    """ NewMart catelogue  item with  protected, validated, stock."""
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self._stock = stock    # encapsulated: change via property only

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, value):
        if value < 0 :
            print(f"Rejected {self.name} stock can not be Negetive")
        else:
            self._stock = value
    def final_price(self):
        return self.price   # base rule: price as-is
item = product("Notebook", 60, 100)
item.stock = -5                       # validation in action
#print(item.name, "| stock:", item.stock, "| final:", item.final_price())


#2. => Project 
class Product:                        # compact base from the last snippet
    def __init__(self, name, price, stock):
        self.name, self.price, self._stock = name, price, stock

    def final_price(self):
        return self.price

class Electronics(Product):
    def final_price(self):
        return self.price * 1.18      # 18% GST on electronics

class Grocery(Product):
    def final_price(self):
        return self.price             # groceries are tax-free here

cart = [Electronics("Headphones", 2500, 10),
        Grocery("Rice 5kg", 450, 80),
        Electronics("Mouse", 900, 15)]

order_total = 0
for item in cart:                     # polymorphism: one loop, many rules
    order_total += item.final_price()
    #print(f"{item.name:10} INR {item.final_price():,.2f}")

#print(f"{'TOTAL':10} INR {order_total:,.2f}")



# project 4=> Fulfilling an Order Through the Property

class Product:
    def __init__(self, name, price, stock):
        self.name, self.price, self._stock = name, price, stock

    @property
    def stock(self):
            return self._stock

    @stock.setter
    def stock(self, value):
        if value >= 0:
            self._stock = value
inventory = [Product("Headphones", 2500, 3), Product("Rice 5kg", 450, 50)]
ordered_qty = {"Headphones": 2, "Rice 5kg": 4}     # dict from Day 10

for item in inventory:
    item.stock = item.stock - ordered_qty[item.name]
    #print(f"{item.name:10} remaining stock: {item.stock}")



# 4. Project => 
class Product:
    def __init__(self, name, price):
        self.name, self.price = name, price

    def final_price(self):
        return self.price
    
class Fashion(Product):
    def final_price(self):
        return self.price * 0.95   # flat 5% fashion discount

cart = [Fashion("Kurta", 1200), Product("Notebook", 60), Fashion("Saree", 3000)]
total = 0
for item in cart:
    total += item.final_price()
#print(f"Cart total: INR {total:,.2f}") 





class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def Details(self):
         return f"{self.name} | INR {self.salary:,.2f}"

class Intern(Employee):
    def __init__(self, name, salary, duration_months):
        super().__init__(name, salary)
        self.duration_months = duration_months

    def Details(self):
        base = super(). Details()
        return base + f" | Intern for {self.duration_months} months "
i = Intern("Shivam Sharma",24000, 6)
print(i.Details())


