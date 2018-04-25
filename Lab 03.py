import pickle
with open("danebin", "wb") as d:
    a = [1, 2, 3, 4, 5]
    b = [9, 10, 11, 12]
    a.append(b)
    pickle.dump(a, d, protocol=1)
d.close()
# d = open("danebin", "rb")
# a = pickle.load(d)
# print(a)
# d.close()