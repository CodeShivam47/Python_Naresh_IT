# Set 
#s = {1,2,3,4,5}
s = {"Hello", "World"}
#print(s)

# add an element in set
s.add("Shivam")
#print(s)

# remove an alement...
s.remove("Hello")
#print(s)

#4 => union of two sets
a = {1,2,3,4}
b = {6,7,8,4}
#print(a.union(b))


# 5=> intersection of two sets
c = a.intersection(b)
#print(c)

# 6 => diffrrence of two set
d = a.difference(b)
#print(d)


# => remove dublicate from set
p = [10,11,12,13,14,15]
q = [10,12,14,16]
c = p + q
d = list(set(c))
print(d)