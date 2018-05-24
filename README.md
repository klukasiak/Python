# Python

## Lab 01.py

### Środowisko PyCharm i podstawy języka Python 

**Zad1** *Zapoznać się z instrukcją laboratoryjną i posługiwaniem się środowiskiem PyCharm, napisać i uruchomić wszystkie podane przykładowe programy.*

**Zad2** *Przyspisać zmiennej s łańcuch złożony z kilkunastu znaków i wyświetlić ten łańcuch od tyłu tj. od ostatniego znaku do początkowego. Wskazówka: len(s)-liczba znaków łańcucha s.*

**Zad3** *Utworzyć listę 20 elementów różnych typów i wyświetlić te elementy, które są łańcuchami. Wskazówka: type(x)- typ wartości x.*

**Zad4** *Utworzyć listę 20 wyrazów i posortować ją leksykograficznie (przy użyciu dowolnej metody).*

## Lab 02.py

### Funkcje i pliki

**Zad1** *Wykonać wszystkie zadania zalecane w instrukcji laboratoryjnej (ma stronie domowej).*

**Zad2** *Napisać program zawierający definicję funkcji przyjmującej zmienną liczbę argumentów liczbowych i obliczającej sumę tych argumentów, a następnie wywołując tę funkcję dla pewnego, ustalonego ciągu liczb.*

**Zad3** *Napisać program, który w bieżącym katalogu tworzy plik o nazwie "liczby", a następnie pobiera od użytkownika wartość naturalną n oraz ciąg n liczby rzeczywistych i zapisuje ten ciąg do pliku "Liczby", oddzielając te liczby spacjami. Po wykonaniu programu obejrzeć przy pomocy edytora tekstowego zawartość utworzonego pliku.*

**Zad4** *Przy użyciu edytowa tekstowego uteorzyć plik zawierający kilkanaście liczb całkowitych poddzielanych od siebie spacjami. Napisać program przyjmujący od użytkownika trzy nazwy plików: jednego istniejącego i dwóch nieistniejących, a następnie rozdzielający zawartość zawartość pierwszego pliku na dwa pozostałe- liczby parzyte do jednego i nie parzyste do drugiego pliku. Przy użyciu edytora tekstowego obejrzeć zawartość obu utworzonych przez program plików.*

**Wskazówka:** *Aby podzielić linię tekstu wczytaną z pliku na jednostki syntatyczne oddzielone ustalonymi znakami można wykorzystać metodą line.splikt('znak').*

## Lab 03.py

### Pliki binarne

**Zad1** *Przy użyciu poniższego programu zapisać w pliku binarnym listę liczb 0,1,...,9 w postaci tekstowej:*

```python
import pickle 
d = open("danebin", "ub") 
a = range(0, 10) 
pickle.dump(a, d) 
d.close() 
```

*Obejrzeć zawartość utworzenego pliku przy użyciu Notatnika.* 

**Zad2** *Przy użyciu poniższego programu wyświetlić zawartość pliku:*

```python
import pickle
d=open("danebin","rb")
a=pickle.load(d)
print(a)
d.close()
```

**Zad3** *W programie zapisującym wprowadzić zmianę: ......protocol=1......, wykonać i ponownie obejrzeć zawartość utworzonego pliku przy użyciu Notatnika.*

**Zad4** *Wyświetlić zawartość utworzonego pliku przy użyciu programu z punktu 2.*

**Zad5** *Przy użyciu programu z punktu 3 utworzyć dwa pliki binarne zawierające dowolne zbiory liczb. Napisać program, który utworzy trzeci plik binarny zawierająccy sumę zawartości dwóch pierwszych plików.*

**Zad6** *Sprawdzić że metody pickle.dump() i pickle.load() działają dobrze również w przypadku bardziej złożonych obieków np. lista list* **Serializacja/deserializacja**

## Lab 04.py

### Programowanie obiektowe w pythonie

**Zad1** *Wykonać wszystkie ćwiczenia zalecone w instrukcji laboratoryjnej.*

**Zad2** *Zdefiniować klasę Pair posiadającą dwa pola będące liczbami całkowitymi, metodę check() wyświetlającą komunikat "Liczby są równe" lub "Liczby są różne". W głownej części programu zainicjować kilka przykładowych obiektów i wypróbować działanie.*

**Zad3** *Zdefiniować klasę Triple dziedziczącą po Pair, zawierającą jedno więcej pole i odpowiednio redefiniującą metodę check(). Wypróbować jak wyżej.*

**Zad4** *Zdefiniować hierarchię klas:*

![diagram here](https://image.ibb.co/ictwrT/Przechwytywanie.png "Prosty diagram")

## Lab 05.py

### Klasy abstrakcyjne i wyjątki

**Zad1** *Wykonać wszystkie ćwiczenia zalecone w instrukcji laboratoryjnej.*

**Zad2** *Zdefiniować klasę abstrakcyjną Pair o dwóch polach liczbowych a,b oraz jednej metodzie abstrakcyjnej operation(self), następnie klasę Creator dziedziczącą po Pair i definiującą operation() jako wyświetlającą max(a,b), a potem utworzyć obiekt klast Creator i wywołać jego metodę.*

**Zad3** *Zdefiniować klasę wyjątku PozaZakresem(Exception) wyświetlającą odpowiedni komunikat oraz klasę Pomiar posiadającą pole liczbowe dana i rzucającą powyższy wyjątek, jeśli dana <-20 lub  dana > 20. W poleceniu try utworzyć kilka obiektów klasy Pomiar i przechwycić ewentualne wyjątki.*

**Zad4** *Rozbudować rozwiązanie zadania 2 tak, aby program pobierał od użytkownika liczbę naturalną n, a następnie pobierał ciąg n danych i dane prawidłowo zapisywał do pliku Pomiary, a dane poza zakresem pomijał, wyświetlając przy tym odpowiedni komunikat.*

**Uwaga:** *Było by dobrze, gdyby program reagował komunikatami również na dane niebędące liczbami.*

## Lab 06.py

### Wyrażenia regularne

**Zad1** *Napisac program, który pobiera od użytkownika linię tekstu (ujętego w znaki "") i wypisuje wszystkie (maksymalne) ciągi cyfr, które są w nim zawarte* 

abf**15**cxd**778**rd**31**zy

**Zad2** *Jak wyżej, zlicza wystąpienia litery "a" w tekście (wyświetla, ile ich jest)*

**Zad3** *Jak wyżej, wypisuje wyrazy (grupy liter ograniczone innymi znakami), które sa conajwyzej trzy literowe.*

**Zad4** *Jak wyżej, wczytuje linię tekstu zwierającą pewną liczbę nazw plików z rozszerzeniami (np. Nazwa1.txt, nazwa5.c, nazwa5.cpp itd.) oddzielonych od siebie spacjami i wypisuje te z nich, które mają rozszerzenie .py Uwaga: Uwaga: nazwa pliku nie może zaczynać się od cyfry, ani zawierać znaku specjalnego*

**Zad5** *Umieścić w pliku tekst wiersza "Kaczka dziwaczka". Napisac program, który na jego pdstawie utrzowy drugi plik, w którym wszystkie grupy liter "kacz" będą zamienione na "pracz" i na odwrót, zaś "Kacz" będzie zamienione na "Pracz" i na odwrót.*
