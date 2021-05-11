Li = [1,2,3,4, "Python", "JS", 3.14, 9.8]

li1 = list([12,125,8,987,65,21])

print(Li)

print(Li[-3])
print(Li[4:6])

print(li1)

li2 = [i**2 for i in range(1,11)]
print(li2)

li3 = [0]*10
print(li3)

li2d = [[0]*3]*3

print(li2d)

li4 = [[1,2,3], [4,5,6]]

# Extend
NewLi = Li + li2 + li4
print(NewLi) 

li = [1,2,3]
print(li)

li.extend([4,5,6])
print(li)

# Append

li.append(7)
print(li)

print(li.index(4))

li.insert(0, 0)
print(li)

li.insert(3,2.5)
print(li)

del li[3]
print(li)

a = li.pop(0)
print(a)
print(li)

li.remove(4)
print(li)

li = [4,9,3,74,152,4,12,3,478,456,44]

#li.sort(reverse=True)
li.sort()
li.reverse()
print(li)

li5 = li.copy()

