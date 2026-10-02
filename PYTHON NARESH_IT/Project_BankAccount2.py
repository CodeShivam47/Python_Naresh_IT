class BankAccount:  # compact version off the class
    def __init__(self, owner, balance = 0.0):
        self.owner = owner
        self.balance = balance

    def withdraw(self, amount):
        if amount <= self.balance: # silenty skip funds are shorts
            self.balance -= amount 

accounts = [ BankAccount("Priya Sharma", 5000),
            BankAccount("Rahul", 4000),
            BankAccount("Sanjay",3000)
            ]
for acct in accounts:
    acct.withdraw(1000)    # early free  attemps on every account

bank_total = 0
for acct in accounts:
    bank_total =+ acct.balance
    print(f"{acct.owner:12} INR {acct.balance:,.2f}")

print(f"SafeBank holds a total of INR {bank_total:,.2f}")







