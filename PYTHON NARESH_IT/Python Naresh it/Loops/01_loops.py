
# => how remone in list

# nums = [1,2,3,4,5]
# for n in nums:
#     if n % 2 == 0 : nums.remove(n)
# print(nums)



# nums = [1 ,2, 3, 4, 5, 6]
# for n in nums:
#     #if n % 2 == 0 : nums .remove(n)
#     if n % 3 == 0 : nums.remove(n)
# print(nums)


# ex => 2
# raw = ['loan approved fast!', 'Fraud alert on card', 'loan approved']
# docs = [d.lover().strip('!').split() for d in raw]
# vocab = list(dict.fromkeys(t for d in docs for t in d))
# stoi = {tok: i for i, tok in enumerate(vocab)}
# ids = [[stoi[t] for t in d] for d in docs]
# pad = [x + [0] * (max - len(x)) for x in ids]

# = > 3

records = [
    {'id': 'c1','tenure':2,'charger':70.5,'plan':'basic','churn':1},
    {'id': 'c2','tenure':48,'charger':95.5,'plan':'premium','churn':0},
    {'id': 'c3','tenure':2,'charger':70.5,'plan':'basic','churn':1},
]


# => drop exact duplicates keep first order occurence...
# seen = set()
# unique_records = []

# for record in records:
#     key = tuple(sorted(record.items()))
#     if key not in seen:
#         seen.add(key)
#         unique_records.append(records)
# print(unique_records)


# => count churn labels with counters -> is the data imbalanced
label_counts = Counter(record["churn"] for record in records)
