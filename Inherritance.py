import math as m

class BasicCalculation:

    def __init__(self, name):
        self.name = name
        print("Hello", name)

    def add(self, x,y):
        return x+y
    
    def subtract(self,x,y):
        return x-y

    def divide(self,x,y):
        return x//y
    
    def multiply(self,x,y):
        return x*y

class AdvancedCalculation(BasicCalculation):

    def __init__(self, name, UserID):
        super().__init__(name)
        self.UserID = UserID
        print("Your User ID is", UserID)

    def sine(self, x):
        return m.sin(x)

    def tangent(self,x):
        return m.tan(x)

    def cosine(self,x):
        return m.cos(x)

    class ScientificCalculation(AdvancedCalculation, BasicCalculation):
        pass



ob = AdvancedCalculation("Rohit", 445)
print(ob.add(5,9))
print(ob.subtract(5,9))
print(ob.divide(5,9))
print(ob.multiply(5,9))
print(ob.cosine(45))




