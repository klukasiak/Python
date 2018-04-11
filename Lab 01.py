s = "ABCDEFG"
print(s)

for i in range(len(s)-1, -1, -1):
    print(s[i], end='')

print('')
lista = [1, 2.3, 'asd', 4, 'bca', 31, 'DDaad', 21, 23, 2334, 'asd', 21, 13, 14, 15, 'jbjdfg', 109, 12, 'sdad', 20]

for i in range(0, len(lista)):
    if type(lista[i]) is str:
        print(lista[i])

words = ['abc', 'bca', 'dca', 'zwa', 'sad', 'obc', 'kia', 'ond', 'zwd', 'dcs', 'jeja', 'xad', 'foa', 'qwe', 'paq', 'orep', 'zxz', 'abc', 'hsj', 'oap']

print(words)
words.sort()
print(words)
