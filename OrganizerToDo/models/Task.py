class Task:

    # zmienne
    nazwa = ""
    dzien = 0
    miesiac = 0
    rok = 0
    wykonane = False
    tresc = ""

    def __init__(self, dzien=0, miesiac=0, rok=0, tresc="", wykonane=False):
        self.dzien = dzien
        self.miesiac = miesiac
        self.rok = rok
        self.wykonane = wykonane
        self.tresc = tresc

