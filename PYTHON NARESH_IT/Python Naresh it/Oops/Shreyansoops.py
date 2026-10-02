#
# class Car:
#     #print("Hello how are you...")
# # a = 13  => Attributes
# # def hello():  => method
#   print("How are you...")

# => Object
#class bags:
#   name = "Not Your Colleges"

#   def details(self):
#     print("hello this is the company whom creates bags")
# reebok = bags()
# campus = bags()
# print(reebok.name)
# print(campus.name)


# reebok.details()


# =>3
# => Constructor
# class Bags:
#     def __init__(self,material,zips,pockets):
#         self.material = material
#         self.zips = zips
#         self.pockets = pockets

#         #print("How are you")
#     #print("hello")
# reebok = Bags("leather",3,42)
# campus = Bags("polister",2,4)


# print(reebok.zips)
# print(campus.material)


 # => Attributes and Method
# class Animals:
#     a = 12  # => class Attributes

#     def __init__(self,name):
#         self.name = name # object / instance attributes

#     def hello(self):  # instance methos ! object method => capture the location of obj
#         print("How Are You may name is {self.name}")
#     @classmethod
#     def details(cls): # class method captures the location of class
#         print(f"How are you {cls.a}")


#     @staticmethod  # it will not target any location
#     def speak():
#         print("Hello Shivam i am static method")
    
# obj = Animals("lion")

# obj.details()




# => 4. inheritance
# class Animals: # this will be our parents class
#     a = 12
#     def __init__(self,name):
#         self.name = name
#     def details(self):
#         print(f" Hello your name is {self.name}")
# class humans(Animals):# child calss
#     pass
# obj = Animals("loin")
# obj2 = humans("harsh")
# obj2.details()
# print(obj2.a)




# ex=>2
# mulilevel inheritance...
# class BagFactory:
#     def __init__(self, material, zips, pockets):
#         self.material = material
#         self.zips = zips
#         self.pockets = pockets
#     def details(self):
#         print("your bags details are:")
#         print(self.material)
#         print(self.zips)
#         print(self.pockets)

# class Reebok(BagFactory):
#     def __init__(self, material, zips, pockets, colour):
#         super().__init__(material, zips, pockets)
#         self.colour = colour

#     def details(self):
#         print(self.colour)
#         return super().details()
# class Campus(Reebok):
#     def __init__(self, material, zips, pockets, colour, size):
#         super().__init__(material, zips, pockets, colour)


# bag1 = BagFactory("lether", 3, 4)
# bag2 = Reebok("polyster",4,2)




# multiple inheritance~
# class Animals:
#     def __init__(self, name):
#         self.name = name
# class humans:
#     def __init__(self, id):
#         self.id = id
# class Robots(Animals, humans):
#     def __init__(self, id, name):
#         humans.__init__(id)
#         Animals.__init__(name)
# Robo = Robots(1,"Alexa")
 

# => Polomorphism

# def hello():
#     print("How are You...")


# def hello():
#     print("what are you doing")

# hello()


# class Animals:
#     def speak(self):
#         print("Animals will not speak")

# class Humans:
#     def speak(self):
#         print("We are humans we can speaks...")

# obj = Animals()
# obj.speak()
# obj2 = Humans()
# obj2.speak()


# method overridding

# class Animals:
#     b = 15
#     def __init__(self,name):
#         self.name = name

#     def detail(self):
#         print(f"Your name is {self.name}")
# class Humans(Animals):
#     a = 23
#     def __init__(self, name):
#         super().__init__(name)

#     def info(self):
#         print(f"your info is {self.name} and this is all we have")
# obj = Humans("Cow")
# obj.info()



# method overloading



# => Encapsulation...

class Factory:
    name = "kia" # public class attributes
    _old = 12 # protected
    def __init__(self,type,tyre,colour):
        self.type = type # public object attributes
        self.tyre = tyre
        self.colour = colour


def details(self): # public method

    print("Hello Your details are:")
obj = Factory("sedan", "MRF", "Black")
obj.name = "maruti"
print(obj.name)
