import math


class Pair:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def check(self):
        if self.x == self.y:
            print("Liczby są równe")
        else:
            print("Liczby są różne")


class Triple(Pair):
    z = 0

    def __init__(self, x, y, z):
        Pair.__init__(self, x, y)
        self.z = z

    def check(self):
        if self.x == self.y & self.x == self.z:
            print("Liczby są równe")
        else:
            print("Liczby są różne")


class Kwadrat:
    a = 0

    def __init__(self, a):
        self.a = a

    def pole(self):
        return self.a*self.a


class Prostokat(Kwadrat):
    b = 0

    def __init__(self, a, b):
        Kwadrat.__init__(self, a)
        self.b = b

    def pole(self):
        return self.a*self.b


class Romb(Kwadrat):
    gamma = 0

    def __init__(self, a, gamma):
        Kwadrat.__init__(self, a)
        self.gamma = gamma

    def pole(self):
        return self.a * self.a * math.sin(math.radians(self.gamma))


class Rownoleglobok(Prostokat, Romb):

    def __init__(self, a, b, gamma):
        Prostokat.__init__(self, a, b)
        Romb.__init__(self, a, gamma)

    def pole(self):
        return self.a * self.b * math.sin(math.radians(self.gamma))


para1 = Pair(2, 3)
para1.check()
para2 = Pair(2, 2)
para2.check()

trojka1 = Triple(1, 2, 3)
trojka1.check()
trojka2 = Triple(1, 1, 1)
trojka2.check()

kwadrat = Kwadrat(3)
print(kwadrat.pole())
kwadrat2 = Kwadrat(5)
print(kwadrat2.pole())

prostokat = Prostokat(3, 4)
print(prostokat.pole())
prostokat2 = Prostokat(5, 2)
print(prostokat2.pole())

romb = Romb(4, 30)
print(romb.pole())
romb2 = Romb(5, 45)
print(romb2.pole())

rownoleglobok = Rownoleglobok(2, 3, 30)
print(rownoleglobok.pole())
rownoleglobok2 = Rownoleglobok(3, 4, 45)
print(rownoleglobok2.pole())
