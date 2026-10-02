# pandas.....=>
import pandas as pd
# s = pd.Series([10, 20, 30, 40, 50])
#print(s)
#print(type(s)) # types of s.....
#print(s.values) # print real values...
#print(s.index)  #  Check range of index....
# s.name = "Number"
# print(s)  # print the all series...




# => 2. inexing
#print(s[0])
#print(s[0:2]) # print only 0 and 1 index
#print(s[2:4])




# => i loc -> location based indexing
#print(s.iloc[3]) # print only one value
#print(s.iloc[[1,3,4]])  => print multiple values


# index = ["apple", "banana", "grapes", "orange", "strawberry"]
# s.index = index
# print(s)

#print(s['grapes'])

# loc -> label based indexing
#print(s.loc['grapes'])

# in label based indexing your start as well as stop value bpth are include in output

#print(s['banana': 'grapes'])


# => 2
fruits_protein = {
    "Avocado": 2.0,
    "blackberries": 3.0,
    "Guava": 2.6,
    "oranges": 0.9,
    "Apples": 0.3,
    "Kiwi": 1.1,
    "pomgranate": 1.7,
    "Mango": 1.8,
    "Cherries" : 1.0
}
s2 = pd.Series(fruits_protein)
#print(s2)


# Conditinal Selection....
#print(s2[s2>1])


# Conditional Operator

#print([(s2  >0.5) & (s2 < 2)])


# modify the Series...

#print(s2[["Mango"] : 4.0])


# => data Frames....
data = {
    "Name": ["Alice", "Bob", "Charlie","david", " Eve", "Alice"],
    "Age": [25, 30, 35, 40, 45, 50],
    "Depertment" : ["HR", "IT", "Finance", "IT", "HR", "HR"],
    "Salary": [2500, 3000, 3500, 4000, 4500, 5000]
}

df = pd.DataFrame(data)
#print(df)

#print(df.head(2))   # first two Value of data frames
#print(df.tail(3))   # Last two value of the data...

# => Using loc and iloc

#print(df.iloc[1:3])  # print first three value

#print(df.loc[1 : 2,["Age","Depertment"]])


# -> Access one particular column.....
#print(df[ "Age"])


# -> Access multipale column.....
#print(df[["Age", "Depertment"]])


# Drop the value
# print(df)
# print(df.drop("Age", axis = 1))


# -> Check the chef of data
#print(df.shape)

# -> Check information of data
#print(df.info())

# -> using Describe function to describr the data

#print(df.describe())



# 3. => Broadcasting...
# s= df["Salary"] = df["Salary"] + 1000
# print(f"{df["Salary"]},and {s}")


# => Renaming rowa and column
# Rename = df.rename(columns = {"Depertment" : "Dept"}, inplace = True)
# print(df)



# => unique value in data
# print(df["Salary"].unique())
# print(df["Depertment"].unique())

# print(df["Depertment"].value_counts())
# df["Promoted Salary"] = df["Salary"] * 20 # addind the promoted Salary...
# print(df)

# => Data Cleaning....

# s = df.isnull().sum()
# print(s)
# df.dropna(how = "any")
# print(s)

# 

# m =df["Age"].fillna(df["Age"].mean())
# print(m)

# name = df["Name"].replace("Charlie", "Rose")  # Replace the name... 
# print(name)


# Dublicates....
# df_dup = df[df.duplicated()]
# print(df_dup)

# 4. Invalid Salary....
# lamda
# m = df["Promoted Salary"] = df["Promoted Salary"].apply(lambda x: x/10 if x > 65000 else x) 
# print(m)


# Joins and merges

# => left =>  right => outer  => ineer

department_info = {
    "Department" : ["HR", "IT", "FINANCE"],
    "Location" : ["New York", "Delhi", "Chicango"],
    "Manager" : ["Laura", "Soma", "Reetu"]
}

df2 = pd.DataFrame(department_info)
#print(df2)

#Pan = pd.concat([df, df2]) # Merge the data

#Pan = pd.concat([df, df2], axis = 1)
 

# importing File







