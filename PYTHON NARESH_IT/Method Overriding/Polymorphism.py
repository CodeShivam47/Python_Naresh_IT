class Cardpayments:
    def  process(self, amount):
        return f"Card charged INR {amount:.2f}"

class UPIPayments:
    def process(self, amount):
        return f"UPI charged INR {amount:.2f}"

class CashPayments:
    def process(self, amount):
        return f" cash Payment Charged INR {amount:.2f}"
payment = [Cardpayments(), UPIPayments(), CashPayments()]
for p in payment:
    print(p.process(999))
     