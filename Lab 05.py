class Pair:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def operation(self):
        pass


class Greater(Pair):
    def operation(self):
        print(max(self.a, self.b))


class PozaZakresem(Exception):
    def __str__(self):
        return "Liczba jest poza zakresem!"


class Pomiar:
    def __init__(self, dana):
        if (type(dana) != int and type(dana) != float) or dana < -20 or dana > 20:
            raise PozaZakresem()
        self.dana = dana


class NieNaturalna(Exception):
    def __str__(self):
        return "Liczba nie jest naturalna"


class Naturalna:
    def __init__(self, n):
        if n < 0 or type(n) != int:
            raise NieNaturalna()
        self.n = n


# wieksza = Greater(8, 2)
# wieksza.operation()
#
# try:
#     pomiar1 = Pomiar(2)
#     pomiar2 = Pomiar(20)
#     pomiar3 = Pomiar(-20)
#     pomiar4 = Pomiar(222)
# except PozaZakresem as pz:
#     print(pz)


try:
    n = Naturalna(int(input('Podaj liczbe naturalna: ')))
except NieNaturalna as nn:
    print(nn)

pomiary = open("pomiary.txt", "w+")

for i in range(0, n.n):
    try:
        pomiar = Pomiar(int(input("Podaj liczbe: ")))
        pomiary.write(str(pomiar.dana))
        pomiary.write(' ')
    except PozaZakresem as pz:
        print(pz)

pomiary.close()

