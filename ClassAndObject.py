class Apollo:

    destination = 'moon'

    def fly(self):
        print('Spaceship is flying')

    def get_destination(self):
        print('Destination is:', self.destination)

ob = Apollo()
print(ob.destination)

ob.fly()
ob.get_destination()

ob.destination = "mars"
ob.get_destination()

ob1 = Apollo()
ob1.get_destination()