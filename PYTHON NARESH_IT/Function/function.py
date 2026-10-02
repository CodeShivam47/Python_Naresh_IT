# Function
# def caculate_invoice_total(amount):
#     gst = amount* 0.18
#     return amount + gst
# print(caculate_invoice_total(2500.0))
# print(caculate_invoice_total(1250.00))



# 2. => 
# def ganerate_payslip(name, basic_salary):
#     hra = basic_salary * 0.40
#     gross = basic_salary + hra
#     print(f"{name}: gross salary Rs {gross:,.2f}")
# ganerate_payslip("priya sharma", 50000)
# ganerate_payslip("shivam sharma", 90000)



# 3. =>

# def salary_summary(basic_salary):
#     hra = basic_salary * 0.40
#     pf = basic_salary * 0.12
#     net = basic_salary + hra - pf
#     return net, hra, pf
# net, hra, pf = salary_summary(5009)
# print(f"Net Rs {net:,.2f} | HRA Rs {hra:,.2f} | PF Rs {pf:,.2f}")
# def log_order(order_id):
#     print("order", order_id, "recorded")

# result = log_order("N1001")
# print(result)



# 4. =>

# def simple_interest( principal, rate, years):
#     return principal * rate * years/100

# interest = simple_interest(100000, 7.5, 2)
# print(interest)


# 5. =>

# def simple_interest(principal, rate, years):
#     return principal * rate * years/100


# def maturity_amount(principal, rate, years):
#     interest = simple_interest(principal, rate, years)
#     return principal + interest

# principal = 100000
# rate = 7.5
# years = 2

# print("Simple interest:",simple_interest(principal, rate, years))
# print("maturity_amount", maturity_amount(principal, rate, years))



# 6. => 
# def open_accounts(name, account_types = "Savings", brance = "Hyderabad"):
#     print(f"{name},  {account_types}, {brance}")

# open_accounts("shivam")
# open_accounts("Shivam", " currants")
# open_accounts("Shivam", "currents", "rewa")



# 7. args

# def cart_total(*amounts):
#     total = 0
#     for amount in amounts:
#         total = total + amount
#     return total
# print(cart_total(1250.50, 899.0))
# print(cart_total(210,500, 800, 100, 1200))
# print(cart_total())


# 8. =>
# def register_customer(name, **details):
#     print("Customer:", name)
#     for key, value in details.items():
#         print(f"{key}, {value}")
# register_customer("Priya sharma", city = "Hyderabad", plan="gold")
# register_customer("Sadhana singh", city="Satna", reffered_by ="Rahul")



# => 9
# def bill_summary(customer, *amounts, discount_percent = 0):
#     bill = sum(amounts)
#     discount = bill*discount_percent/100
#     payable = bill-discount
#     print(f"Customer: {customer}")
#     print(f"bill : {bill:,.2f}")
#     print(f"payable Amount: {payable:,.2f}")

# bill_summary("Newmart Customer", 1200, 25000, 850)

# => 9
# def apply_discount(price):
#     discount = price * 0.10
#     return price - discount
# print(apply_discount(1000))
# store_name = "Jop Mart"

# def print_receipt(amount):
#     print(f"{store_name}: Rs {amount:,.2f}")
# print_receipt(900)



# 10. =>
# add_gst = lambda amount: amount * 1.18

# print(add_gst(100))
# print(add_gst(2500))


# def add_gst_full(amount):
#     return amount * 1.18

# print(add_gst_full(1000))

# 



# 11 -> 
# def net_salary(basics: float, bonus: float = 0.0 ) -> float:
#     pf = basics * 0.12
#     return basics + bonus - pf
# print(net_salary(50000))
# print(net_salary(50000.0, 50000))
# print(net_salary(40000))



# 12 =>
# def clean_price(raw_price: str) -> float:
#     """Convert messy price text like '1,299.50' or 'Rs 450' to a float"""
#     cleaned = raw_price.replace("Rs", "").replace(",", "").strip()
#     return float(cleaned)
# print(clean_price("1,299.50"))
# print(clean_price("Rs 24,999.00"))
# print(clean_price("   450 "))

