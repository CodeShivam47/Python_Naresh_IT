class EmailSender:
    def send(self, msg):
        return "Email : "+ msg

class SMSSender:
    def send(self, msg):
        return "SMS :>" +msg
class AlertService(EmailSender, SMSSender):
    pass
alert = AlertService()
print(alert.send("Payment Received..."))
print(AlertService.__mro__)
