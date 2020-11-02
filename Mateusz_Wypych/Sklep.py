class Produkt:
    nazwa = ""
    ilosc = None  # ilosc na magazynie
    cena = 0.0

    def __init__(self, nazwa=None, ilosc=None, cena=None):
        self.nazwa = nazwa
        self.ilosc = ilosc
        self.cena = cena

    def __str__(self):
        return 'Nazwa produktu: {s.nazwa} | Ilosc sztuk na magazynie: {s.ilosc} | Cena: {s.cena}'.format(s=self)

    def __add__(self, other):
        if self.nazwa == other.nazwa:
            self.ilosc = self.ilosc + 1
            self.cena = self.cena
            self.nazwa = self.nazwa
            return Produkt(self.nazwa, self.ilosc, self.cena)
        else:
            print("Nie mozna dodac dwoch roznych prouktow")

    def zmienCene(self, c):
        print(f'Cena przed zmianą: {self.cena}')
        try:
            self.cena = float(c)
        except ValueError:
            print("Podales zla cene")

        print(f'Cena po zmianie: {self.cena}')

    def dodajProdukt(self):
        self.ilosc = self.ilosc + 1


p1 = Produkt("Maslo", 30, 6.50)
print(p1)

p2 = Produkt("Maslo", 1, 6.50)
p3 = Produkt("Mleko", 39, 2.50)

print(p3)

for i in range(10):
    p3.dodajProdukt()

print(p3)

p1 = p1 + p2
print(p1)

p2.zmienCene("jajko")
p3.zmienCene(3.5)


