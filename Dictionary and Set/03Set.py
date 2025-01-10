s1 = {1, 2, 54, 69}
s2 = {5, 6, 11, 69}
e = set() #Dont use s1= {} as it will create an dictionary

print(s1)

s1.add(554)

print(s1, type(s1))

print(s1.union(s2))

print(s1.intersection(s2))