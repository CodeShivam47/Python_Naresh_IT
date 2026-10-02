# => Hotel management system

# Class and Object
class Room:
    def __init__(self, room_no, room_type, price):
        self.room_no = room_no
        self.room_type = room_type
        self.price = price
room1 = Room(101,"Deluxe","2500")
room2 = Room(102,"Standard","1500")

#Room => class
# room 1 and room2 => object

# 2. =>  Encapsulation

class Customer:
    def __init__(self, name, phone):
        self.name = name

        self.__phone = phone # the number is private Attributes
    def get_phone(self):
        return self.__phone

customer = Customer("Shivam","7723051014")
print(customer.get_phone())

# 3.  => Inheritance.....

class Person:
    def __init__(self,name):
        self.name = name

    def display(self):
        print("Name:",self.name)

class Customer(Person):
    def book_room(self):
        print(self.name,"booked a room")


customer = Customer("Shivam")
customer.display()
customer.book_room()



# => polymorphism

class StandardRoom:
    def room_service(self):
        print("Standard room services...")


class DeluxeRoom:
    def room_service(self):
        print("Deluxe room sevice with additional facilities..")


rooms = [StandardRoom(),DeluxeRoom()]
for room in rooms:
    room.room_service()



# 5. => Abstraction
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CashPayment(Payment):
    def pay(self, amount):
        print("Paid RS:", amount, "by cash")

class CardPayment(Payment):
    def pay(self, amount):
        print("paid RS:", amount, "by card")

Payment = CashPayment()
Payment.pay(2500)
        






    