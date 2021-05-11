S = {"Mango", "Cheery", "Papaya", "Mango"}


S.add("Banana")

S.remove("Cheery")
print(S)


S1 = {1,2,3,4,5,6,7,8,9,10,11,12,13}

S2 = {4,5,7,3,8,11,13}

print(S2.issubset(S1))

print(S2.union(S1))

print(S2.intersection(S1))

print(S2.symmetric_difference(S1))