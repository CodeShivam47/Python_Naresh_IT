# student = {"name": "shivam",
#            "class" : "VII"}
# print(student)

records = [
    {
        'id':'c1','tenure':2,'charges':70.5,'plan':'basic','churn':1
        },
    {
        'id':'c2','tenure':3,'charges':60.5,'plan':'preamiun','churn':0
        },
    {
        'id':'c3','tenure':4,'charges':80.5,'plan':'Advance','churn':3
        }
    ]

# print(records)

# print(records.copy())
# print(records.pop(0))
# print(records.index())
# print(records.copy())
unique_records = []
seen = set()
for record in records:
    record_tuple =tuple(sorted(records.items()))
if record_tuple in seen: