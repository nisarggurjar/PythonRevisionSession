t = (1, 'Nisarg', "Python")
t1 = (112,541,12,11,112,45,541,1112,112,11,45)
#t[1] = "Nisarg Gurjar"

print(t.index("Nisarg"))

print(t1.count(11))

t = list(t1)
t[1] = "Nisarg Gurjar"
t = tuple(t)
print(t)