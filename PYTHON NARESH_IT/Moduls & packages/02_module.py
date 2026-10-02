import os

os.makedirs("fianance_tools", exist_ok=True)  # the package folder
# Create an empty __init__.py — its presence marks the folder as a package

with open("finance_tools/__init__.py", "w") as f:
    pass

print(os.listdir("finance_tools"))



#%%writefile finance_tools/tax.py

def gst(amount, rate=0.18):
    """Return only the GST portion of a bill."""
    return amount * rate

def net_price(amount, rate=0.18):
    return amount + gst(amount, rate)

if __name__ == "__main__":
    print(net_price(1000))      

