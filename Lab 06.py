import re

# ciag = input("Podaj ciag znakow")
ciag = "\"AJD12389dda1989a9183fd19239128asjkjakj18askdjj12ajdk\""
liczby = re.findall(r"\d+", ciag)
iloscA = len(re.findall(r"a", ciag))
slowa = list(filter(None, re.findall('(?<![a-zA-Z])[a-zA-Z]{1,3}(?![a-zA-Z])', ciag)))

pliki = "bieda.txt essa.es skrypt.py da123.c sk.py"
rozszerzeniePy = re.findall(r"\w+" + r".py", pliki)

wiersz = open("kaczkaDziwaczka.txt", "r+")
wierszEdited = open("kaczkaDziwaczkaEdit.txt", "w+")

for linia in wiersz:
    if re.findall(r"kacz", linia):
        zmienionaLinia = re.sub(r"kacz", "pracz", linia, re.IGNORECASE)
    else:
        zmienionaLinia = re.sub(r"pracz", "kacz", linia, re.IGNORECASE)
    wierszEdited.write(zmienionaLinia)
