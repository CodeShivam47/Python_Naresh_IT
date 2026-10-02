class StockItem:
     def __init__(self, name, price, stock):
          self.name = name 
          self.price = price
          self.stock = stock
          
data = [("Headphones", 2500, 4), ("Rice 5kg", 450, 80),
        ("Notebook", 60, 200), ("Webcam", 1800, 7)]

items = []
for name, price, stock in data:
     items.append(StockItem(name, price, stock))
total_value = 0
low_stock = []
for item in items:
     total_value += item.price * item.stock
     if item.stock < 10:
          low_stock.append(item.name)

print(f"total inventory value INR :{total_value:,.2f}")
print(f"Low_stock items (below 10):", low_stock)