def suma_liczb(*liczby):
    suma = 0
    for j in liczby:
        suma += j
    return suma


print(suma_liczb(2, 3, 4, 5, 6))

plikLiczby = open("Liczby.txt", "w+")
ilosc = input("Podaj ile chcesz wpisac liczb")
liczba = 0
for i in range(0, int(ilosc)):
    liczba = input("Podaj liczbe: ")
    plikLiczby.write(liczba)
    plikLiczby.write(' ')
plikLiczby.close()

calkowite = open("calkowite.txt", "r")
parzyste = open("parzyste.txt", "w+")
nieparzyste = open("nieparzyste.txt", "w+")

line = calkowite.read()
liczbyCalkowite = line.split(' ')
print(liczbyCalkowite)

for i in liczbyCalkowite:
    if(int(i) % 2 == 0):
        parzyste.write(i)
        parzyste.write(' ')
    else:
        nieparzyste.write(i)
        nieparzyste.write(' ')

calkowite.close()
parzyste.close()
nieparzyste.close()
