import math


class Kalkulator:
    print("-----KALKULATOR-----""\n")

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def menu(self):
        print("1.Dodawanie""\n"
              "2.Odejmowanie""\n"
              "3.Mnozenie""\n"
              "4.Dzielenie""\n"
              "5.Pierwiastek z liczby a""\n"
              "6.Pierwiastek z liczby b""\n"
              "0.Wyjscie""\n")
        return int(input("Wpisz liczbe 0-6 : "))

    def dodawanie(self):
        return self.a + self.b

    def odejmowanie(self):
        return self.a - self.b

    def mnozenie(self):
        return self.a * self.b

    def dzielenie(self):
        return self.a / self.b

    def pierwiastekA(self):
        return math.sqrt(self.a)

    def pierwiastekB(self):
        return math.sqrt(self.a)

def main():
    try:
        a = int(input("Podaj liczbe a: "))
        b = int(input("Podaj liczbe b: "))

        kalkulator = Kalkulator(a, b)
        dzialanie = kalkulator.menu()

        if dzialanie == 0:
            print("Do zobaczenia! :)")

        elif dzialanie == 1:
            kalkulator.dodawanie()
            print(f"Wynik dzialania : {kalkulator.a} + {kalkulator.b} = {kalkulator.dodawanie()}")

        elif dzialanie == 2:
            kalkulator.odejmowanie()
            print(f"Wynik dzialania : {kalkulator.a} - {kalkulator.b} = {kalkulator.odejmowanie()}")

        elif dzialanie == 3:
            kalkulator.mnozenie()
            print(f"Wynik dzialania : {kalkulator.a} * {kalkulator.b} = {kalkulator.mnozenie()}")

        elif dzialanie == 4:
            kalkulator.dzielenie()
            print(f"Wynik dzialania : {kalkulator.a} / {kalkulator.b} = {kalkulator.dzielenie()}")

        elif dzialanie == 5:
            if kalkulator.a < 0:
                print("Nie mozna policzyc pierwiastka z liczby ujemnej")
            else:
                kalkulator.pierwiastekA()
                print(f"Pierwiastek z liczby  {kalkulator.a}  = {kalkulator.pierwiastekA()}")

        elif dzialanie == 6:
            if kalkulator.b < 0:
                print("Nie mozna policzyc pierwiastka z liczby ujemnej")
            else:
                kalkulator.pierwiastekB()
                print(f"Pierwiastek z liczby  {kalkulator.b}  = {kalkulator.pierwiastekB()}")

    except ValueError:
        print("Podales STRING, a powinien  byc INT")
    except ZeroDivisionError:
        print("Nie dzielimy przez 0")


if __name__ == "__main__":
    main()
