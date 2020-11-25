class Task:

    # zmienne
    nazwa = ""
    dzien = 0
    miesiac = 0
    rok = 0
    wykonane = False

    def __init__(self, nazwa=None, dzien=0, miesiac=0, rok=0, wykonane=False):
        self.nazwa = nazwa
        self.dzien = dzien
        self.miesiac = miesiac
        self.rok = rok
        self.wykonane = wykonane

