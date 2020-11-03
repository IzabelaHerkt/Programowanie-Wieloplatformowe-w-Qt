#wczytanie tekstu wyswietlenie go ,a nastepnie wyswietleni go od tylu

#count = len(tekst)
#print(count)
#tekst = " "

tekst = input("Podaj tekst: ")

while len(tekst) == 0:
    if len(tekst) == 0:
        print("Nie podano zadnego tekstu")
        tekst = input("Podaj tekst: ")
else:
    print(f"Podany tekst: {tekst}")
    print(f"Odwrocony tekst: {tekst[::-1]}")


