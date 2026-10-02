# 1. Dumps =>
# import json
# orders = {"order_is": 1001, "name":"priya sharma", "Amount":1250.00,
#            "paid": True}
# text = json.dumps(orders, indent=2)
# print(text)    # Python dict -> JSON text
# print(text)
# print(type(json)) 

# # 2. Loads
# back = json.loads(text)              # JSON text -> Python dict
# print(back["name"], back["Amount"])


# 3. =>  Writing and reading JSON files

# import json

# summary = {"store": "NeoMart Pune", "date": "2026-08-12",
#            "total_sales": 2905.75}

# with open("summary.json", "w") as f:
#     json.dump(summary, f, indent=2)      # write JSON straight to a file

# with open("summary.json", "r") as f:
#     loaded = json.load(f)                # read it back as a dict

# print(loaded["store"], "->", f"Rs {loaded['total_sales']:,.2f}")



# 4.=> Mini-project: NeoMart sales file pipeline

# import csv
# from pathlib import Path
# Path("Sales_raw.csv").write_text(
#     "order_id,product,amount\n"
#     "1001,Rice Bag,1250.50\n"
#     "1002,Cooking Oil,\n"
#     "1003,Tea Pack,310.25\n"
#     "1004,Sugar,oops\n"
#     "1005,Atta,455.75\n"
# )

# total , valid, skipped = 0.0, 0, 0
# with open("Sales_raw.csv", newline="") as f:
#     for row in csv.DictReader(f):
#         text = row["amount"].strip()
#         if text and text.replace(".", "", 1).isdigit():
#             total += float(text)
#             valid += 1
#         else:
#             skipped += 1
# print("Valid Orders ", valid, "| Skipped", skipped)
# print("Total sales: Rs {total:.,2f} ")



# Step-2 : publish the results as a JSON summary file
# import json

# # Values computed in Step 1
# summary = {"store": "NeoMart", "date": "2026-08-12",
#            "valid_orders": 3, "skipped_rows": 2, "total_sales": 2016.5}

# with open("sales_summary.json", "w") as f:
#     json.dump(summary, f, indent=2)

# with open("sales_summary.json", "r") as f:
#     print(f.read())



# 4. -> 
# import json
# patients = [
#     {"id": "P101", "name": "Anita Desai", "bill": 4500.0},
#     {"id": "P102", "name": "Rahul Verma", "bill": 12750.5},
# ]

# with open("bills.json", "w") as f:
#     json.dump(patients, f, indent=2)

# with open("bills.json", "r") as f:
#     loded = json.load(f)
# total = 0
# for p in loded:
#     total += p["bill"]
# print("Patients:", len(loded)," Total_Bills Rs:", f"{total:,.2f}")

# AP -1 =>
# with open("Attendence.txt", "w") as f:  # "w": start a fresh log
#     f.write("2026-08-10 Priya Sharma IN 09:02\n")
#     f.write("2026-08-10 Rahul Verma IN 09:15\n")

# with open("Attendence.txt","a") as f:
#     f.write("2026-08-10 Anita Desai IN 09:27\n")

# count = 0

# with open("Attendence.txt") as f:
#     for line in f:
#         count += 1
#         print(count, "|", line.strip())
# print("entries logged:", count)




# Ap => 4 

# from pathlib import Path
# rx = Path("prescription.txt")
# rx.write_text("P101 Anita Desai: Paracetamol 500mg x 10\n"
#               "P102 Rahul Verma: Amoxicillin 250mg x 15\n")
# lines = rx.read_text().strip().split("\n") 
# print("Exists: =>", rx.exists())
# print("Name: => ", rx.name)
# print("Suffix: =>", rx.suffix)
# print("Prescriptions:", len(lines))



#AP3 — NeoMart stock value (CSV write + read + convert)

# import csv
# stock = [
#     {"product": "Rice Bag 25kg", "price": "2450.00", "qty": "14"},
#     {"product": "Cooking Oil 5L", "price": "1120.50", "qty": "8"},
#     {"product": "Tea Pack", "price": "640.00", "qty": "25"},
# ]

# with open("stock.csv", "w", newline="") as f:
#     writer = csv.DictWriter(f, fieldnames=["product", "price", "qty"])
#     writer.writeheader()
#     writer.writerows(stock)

# grand_total = 0.0
# with open("stock.csv", newline="") as f:
#     for row in csv.DictReader(f):
#         value = float(row["price"]) * int(row["qty"])   # strings -> numbers
#         grand_total += value
#         print(f"{row["product"]:<16},Rs {value:>10,.2f}")
# print(f"{'TOTAL':<16} Rs {grand_total:>10,.2f}")


# Last => AP5 — Challenge: MediCare billing pipeline (messy CSV → clean CSV + JSON summar