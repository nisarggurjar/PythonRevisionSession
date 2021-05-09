X = 'hello to ALL'

Y = str("Welcome to Python's Class")

Z = 'Good Afternoon'

print(X[1])
print(X[-3])

a = X[-3]
print(a)

print(Y +' ' + X + ' ' + Z)

print(X*5)

# Slicing

print(Y[0:7])

print(Y[8:10])

print(Y[11:])

print(Y[:7])

print(X[::2])

print(X[::-1])

print(list(X))

print(X.split())
print(X.split('o'))

print(X.capitalize())

print(X.casefold())

print(X.index('t'))

a = "Hello, My name is {1}. i am pursuing {0}"

name = input("Enter your name")
course = input("Enter your course")

print(a.format(course,name))
