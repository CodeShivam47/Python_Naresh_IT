# 1.-># NeoMart: save a daily summary to a text file
# reports = open("Daily_reports.txt", "w")   # "w" = write mode (creates the file)

# reports.write("NewMart Daily Reports\n") # someone write to the file...
# reports.write("total sale NewMart : Rs => 24000000\n")
# reports.close()


# # Read the same file back
# reports = open("Daily_reports.txt", 'r')
# content = reports.read()
# reports.close()
# print(content)




# 2. -> with statements...

# with open("Welcome.txt", "w") as f:
#     f.write("Welcome to SAFEBANK Netbankig...\n")
# with open("Welcome.txt", "r") as f:
#     print(f.read().strip())


# print("File Closed", f.closed)  # True - with closed it for us


 # 4-> Append to the file...


# with open("transactions.txt", "w") as f:
#     f.write("2026-08-10 Deposit  Rs 5,000.00\n")

# with open("transactions.txt", "a") as f:   # "a" = append
#     f.write("2026-08-11 Withdraw Rs 1,200.00\n")

# with open("transactions.txt", "r") as f:
#     print(f.read().strip())



# 5. => Reading files line by line

# with open("customers.txt", "w") as f:
#     f.write("Priya Sharma\nRahul Verma\nAnita Desai\n")

# with open("customers.txt", "r") as f:
#     first = f.readline()   # reads ONE line (with its \n)
#     print("first", first.strip())  # strip() removes the \n

# with open("customers.txt", "r") as f:
#     for line in f:
#         print("Customres", line.strip())

#

# 6. => File paths with pathlib
# from pathlib import Path

# notes = Path("branch_notes.txt")     # a Path object, not just a string
# notes.write_text("SafeBank Andheri branch: 42 new accounts\n")

# print("Exists:", notes.exists())
# print("Name:  ", notes.name)
# print("Suffix:", notes.suffix)
# print("Content:", notes.read_text().strip())


#1 . Excversice

# orders = ["1001,Rice Bag,1250.50", "1002,Oil,890.00", "1003,Tea,310.25"]

# with open("orders.txt", "w") as f:
#     for line in orders:
#         f.write(line + "\n")

# count = 0
# with open("orders.txt", "r") as f:
#     for line in f:
#         count += 1
# print("Orders saved:", count)




# 2. =>
# CSV Files with the csv Module

# import csv

# sales = [
#     {"order_id":"1000", "Name":"Priya", "amount": "12500"},
#     {"order_id":"1001", "Name":"Shatya", "amount": "13500"},
#     {"order_id":"1002", "Name":"Shakshi", "amount": "14500"},
# ]

# with open("daily_salse.csv",  "w", newline="") as f:
#     writer = csv.DictWriter(f,fieldnames=["order_id", "Name", "amount"])
#     writer.writeheader() # first line: column names
#     writer.writerows(sales) # one CSV line per dict

# with open("daily_salse.csv", "r") as f:
#     print(f.read().strip())
    



# 3 =>  Reading CSV with DictReader

# import csv
# from pathlib import Path
# Path("daily_sales.csv").write_text(
#     "order_id,product,amount\n"
#     "1001,Rice Bag,1250.50\n"
#     "1002,Cooking Oil,890.00\n")

# with open("daily_sales.csv", newline="") as f :
#     for row in csv.DictReader(f):  # each row becomes a dict
#         amount = float(row["amount"]) # CSV values are always string
#         print(row["order_id"], row["product"],f"Rs {amount:,.2f}")


# 4 =>  Validating rows before trusting them
# import csv 
# from pathlib import Path

# Path("daily_sales.csv").write_text(
#     "order_id,product,amount\n"
#     "1001,Rice Bag,1250.50\n"
#     "1002,Cooking Oil,\n"          # missing amount
#     "1003,Tea Pack,abc\n"          # invalid amount
#     "1004,Sugar,455.75\n"
# )

# clean_rows, skipped = [], 0
# with open("daily_sales.csv", newline="") as f:
#     for row in csv.DictReader(f):
#         text = row["amount"].strip()
#         if text and text.replace(".", "", 1).isdigit():
#             row["amount"] = float(text)
#             clean_rows.append(row)
#         else:
#             skipped += 1
#     for row in clean_rows:
#         print(row["order_id"], row["product"], row["amount"])
#     print("Skipped_roe", skipped)


# 5.=> Excersice

# import csv
# from pathlib import Path

# Path("payroll.csv").write_text(
#     "name,salary\nPriya Sharma,55000\nRahul Verma,\nAnita Desai,62500\n"
# )

# valid, skipped = [], 0
# with open("payroll.csv", newline="") as f:
#     for row in csv.DictReader(f):
#         if row["salary"].strip().isdigit():
#             valid.append(row)
#         else:
#             skipped += 1

# with open("payroll_clean.csv", "w", newline="") as f:
#     writer = csv.DictWriter(f, fieldnames=["name", "salary"])
#     writer.writeheader()
#     writer.writerows(valid)

# print("Valid:", len(valid), "| Skipped:", skipped)
# with open("payroll_clean.csv") as f:
#     print(f.read().strip())




# Day 28. => JSON and a Sales File Pipeline


