a = int(input())
b = int(input())

try:
    print(a/b)
    print(a*c)
except ZeroDivisionError:
    print("Number is not divisible 0")
except NameError:
    print("A variable is not defined")
except:
    print("an error occurred")
finally:
    print("Thank you")