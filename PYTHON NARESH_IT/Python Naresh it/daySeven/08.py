# Warm ups
# raw_values = ["100", "oops", "250"]
# total = 0
# for raw in raw_values:
#     try:
#         total  = total + int(raw)
#     except ValueError:
#         continue
#     print("total :", total)



# write a small text file 
# with open("File.txt", "w") as f:
#     f.write("AI launchpaid...\n")
#     f.write("Hello, I Am Raftar...\n")

# # raed it back
# with open("file.txt", "r") as f:
#     content = f.read()
#     print(content)


# # raed line by line
# with open("file.txt", "r") as f:
#     for i, line in enumerate(f, start = 1):
#         print(i, " => ", line.strip())


 # write the file
# with open("Tools.txt", "w") as f:
#     f.write("1. gooole gemini..\n")
#     f.write("2. Chat GPT \n")
#     f.write("3. claude..\n")
# # read the file
# with open("Tools.txt", "r") as f:
#      cont = f.read()
#      print(cont)

# # read code line by line
# with open("Tools.txt", "r") as f:
#      for i, line in enumerate(f, start = 1):
#           print(i, "=> ", line.strip()) 





# import csv
# # First, write a small customer csv
rows = [
        {"customerID": "0001", "tenure": "5", "MonthlyCharges": "70.53", "Churn" : "N0"},
        {"customerID": "0002", "tenure": "4", "MonthlyCharges": "80.53", "Churn" : "YES"},
        {"customerID": "0003", "tenure": "3", "MonthlyCharges": "90.53", "Churn" : "N0"},
        {"customerID": "0004", "tenure": "2", "MonthlyCharges": "60.53", "Churn" : "YES"},    
     ]
# with open("customers.csv", "w", newline= "") as f:
#     writer = csv.DictWriter(f, fieldnames=["customerID", "tenure", "MonthlyCharges", "Churn" ])
#     writer.writeheader()
#     writer.writerows(rows)
# print("customers.csv written with", len(rows), "rows.")

# # Now read it back with dictReader - each rows in dict
# with open("customers.csv", "r") as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         print(row["customerID"], "| tenure: ", row["tenure"], "| Churn: ", row["Churn"])






# import csv
# total = 0
# churned = 0
# with open("customer.csv", "r") as f:
#     for row in csv.DictReader(f):
#         total = total + 1
#         if row["Churn"] == "Yes":
#             churned = churned + 1
# rate = churned/ total * 100
# print(f"churned {churned} of {total} customers => churn rate = {rate:.1f} %")




