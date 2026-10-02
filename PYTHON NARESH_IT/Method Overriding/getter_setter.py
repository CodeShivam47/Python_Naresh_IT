# class Doctor:
#     def consultation_fee(self):
#         return 500

# class Specialist(Doctor):
#     def consultation_fee(self):
#         return 1200

# doctors = [Doctor(), Specialist(), Doctor()]
# total = 0
# for d in doctors:
#     total += d.consultation_fee()
# print(f"Total fees collected: INR {total:,.2f}")




# class BankAccount:
#     def __init__(self, owner, balance, pin):
#         self.owner = owner                #public: fine to use anywhere
#         self.balance = balance            #protected: internal, by convention
#         self.pin = pin                    #private: Python renames it
# acct = BankAccount("Priya Sharma", 100000, 471500)
# print(acct.owner)
# print(acct.balance) # works, but you SHOULD not do this
# print(acct.pin)



 # getter and setter controlled access....