class New:

    var1 = "Hello"
    var2 = "Python"
    __secretCode = "74fds845dsfsd645dsfdr4r"

    def get_code(self):
        print("code is", self.__secretCode)


ob = New()
print(ob.var1)
print(ob.var2)
print(ob.get_code())
ob.__secretCode = "Java"
print(ob.var2)