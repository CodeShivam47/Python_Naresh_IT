# class Animals:
#     def __init__(self,name):
#         self.name =  name
#     def __str__(self):
#         return f"Hello my name is {self.name}"
# obj = Animals("lion")
# obj2 = Animals("Tiger")
# print(obj)
# print(obj2)





# 1. => args and kargs
# def addition(*args):
#     s = 0
#     for i in args:
#         s = s + i
#     return s
#     #return args
# print(addition(30,50,20))



#2. kargs=>
# def info(**kwargs):
#      return kwargs
# print(info(name = "Akasrh", age = 24, profession = "Data scientist"))



# a = 15
# print("Even number....") if a % 2 == 0  else  print("odd Number")

# turnery operator



# 3. =>
#a = [1,2,3,4,5,6,7,8,9,10,11, 12,13, 14]
# b = []
# for i in a:
#     if i % 2 ==0:
#         b.append(i)
# print(b)

#b = [i for i in a if i % 2 == 0]
#print(b)




# a = ["sharthak", "harsh", "vedant", "Aakash"]
# # for i in a:
# #     print(len(i))

# lengths =list(map(len,a))
# print(lengths)



