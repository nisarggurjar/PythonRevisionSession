class Apollo:

    destination = 'moon'

    def __init__(self,name):
        self.name = name
        print("Constructor is working")

    def fly(self):
        print('Spaceship is flying')

    def get_destination(self):
        print('Destination is:', self.destination)

    def __del__(self):
        print("Destructor is working")

ob = Apollo("ABC")
print(ob.name)

del ob

print(ob.destination)


