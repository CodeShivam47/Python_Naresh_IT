class Order:
    def __init__(self, order_id, items):
        self.order_id = order_id
        self.items = items
        self.status = "Placed"  # sensible default like support ticket

    def Dispatce(self):
        self.status = "Dispatch"

    def Delivered(self):
        self.status = ("Delivered")

    def track(self):
        return f"Order : {self.order_id}({self.items}) : {self.status}"
o = Order(10001, "Wareless Mouse")
A = Order(101, "Chips")
print(A.track())
A.Dispatce()
print(A.track())
A.Delivered()
print(A.track())
    