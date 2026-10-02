class FixedDeposit:
    rate = 0.07                       # class attribute: one rate for all FDs

    def __init__(self, owner, amount):
        self.owner = owner
        self.amount = amount

    def maturity_amount(self, years):
        return self.amount + self.amount * FixedDeposit.rate * years

    @classmethod
    def from_string(cls, text):
        owner, amount = text.split(",")
        return cls(owner, float(amount))

fd = FixedDeposit.from_string("Anita Desai,200000")
print(f"{fd.owner} matures's FD at INR {fd.maturity_amount(3):,.2f} after 3 years")