import pandas as pd
#df = pd.DataFrame({"city": ["Mumbai", "Delhi"],"revenue":[78, 64]})
#print(type(df))   # instance of the data frame class

#print(df.shape)   # df. shape .... an atributes 
#print(df["revenue"] .mean()) #  its calculate avarages...





# => 2
class BankAccount:
    bank_name = "National Bank"

    def _init_(self, holder : str, balance: float = 0.0):
        self.holder = holder # instance attributes
        self.balance = balance # 

        def deposit(self, amount:float):
            if amount <= 0:
                raise ValueError("Please deposit mony into your account")
            self.balance += amount

        def withdraw(self, amount:float):
            if amount>self.balance:
                raise ValueError("insufficient funds")
            self.balance -= amount



# => 3
class Account:
    def _init_(self, holder, balance = 0.0, manager ="unissigned"):
        self.holder, self.balance = holder, balance

        def monthly_fee(self):
            return 100.0
        class SalaryAccount(Account):
            def _monthly_fee(self):
                return 0.0 # overriding
        class PremiumAccount(Account):
            def _init_(self, holder, balance=0.0, premium = 0.0):
                super()._init_(holder,balance)
                self.manager = manager

            def _monthly_fees(self):
                return 100.0 + super().monthly_fee()

            for a in [Account("A"), SalaryAccount("B"), PremiumAccount("C",10000)]: