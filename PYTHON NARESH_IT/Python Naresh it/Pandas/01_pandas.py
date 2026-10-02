
# 1> 1
# import pandas as pd
# # load the csv into a DataFram - One line
# df = pd.read_csv("customers.csv")
# # Explore  you it  (you'all do this constantly)
# print("Shape (rows, cols):", df.shape)
# print()
# print(df.head())
# print()
# print("Columns:", list(df.columns))



# 2=>
# import pandas as pd

# df = pd.read_csv("customers.csv")

# # Churn rate in pandas  - TWO lines vs the manual loop above
# churn_rate = (df["Churn"] == "Yes").mean() * 100
# print(f"Churn rate (pandas) : {churn_rate:.1f}%")

# # bonus one liner pandas given you for free:
# print("\n Value counts:")
# print(df["Churn"].value_counts())
# print("\nAverage monthly Charge: ",round(df["MonthlyCharges"].mean(),2))



# => 3
import csv, pandas as pd
# Step -1. create a reacher data set (12 customers)
data = [
    ("0001", "5", "70.35", "No"),
    ("0002", "4", "72.35", "Yes"),
    ("0003", "6", "74.35", "No"),
    ("0004", "7", "60.35", "Yes"),
    ("0005", "8", "50.35", "No"),
    ("0006", "9", "80.35", "Yes"),
    ("0007", "0", "90.35", "No"),
    ("0008", "53", "40.35", "Yes"),
    ("0024", "22", "30.35", "No"),
    ("0024", "2", "50.35", "Yes"),
    ("0044", "1", "10.35", "No"),
]
# with open("text.csv", "w", newline="") as f:
#     w = csv.writer(f)
#     w.writerow(["custonerID", "tenure", "MonthlyCharges","Churn"])
#     for r in data:
#         w.writerow(r)
# print("Wrote", len(data), "customers.")

df = pd.read_csv("text.csv")
#print("Shape:", df.shape)
#
# print(df.head())
print("\nChurn breakdown:")
print(df["Churn"].value_counts())

