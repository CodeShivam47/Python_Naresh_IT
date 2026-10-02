# import  math
# from math import sqrt
# import math as m

# print(math.floor(7.8))
# print(sqrt(124))
# print(m.pi)



# import payroll_utils
# salary = 850000
# print(f"Monthly pay: INR {payroll_utils.monthly_pay(salary):,.2f}")
# print(f"Bonus (5-star): INR {payroll_utils.annual_bonus(salary, 5):,.2f}")


#%%writefile discount_utils.py
# discount_utils.py — NeoMart pricing helper

# def final_price(price, pct):
#     """Return price after a pct percent discount."""
#     return price * (1 - pct / 100)

# if __name__ == "__main__":
#     print(final_price(1000, 10)) 


from discount_utils import final_price

cart_total = 4599
print(f"Payable after 15% off: INR {final_price(cart_total, 15):,.2f}")
