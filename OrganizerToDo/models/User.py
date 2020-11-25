class User:

    # zmienne
    imie = ""
    nazwisko = ""
    login = ""
    haslo = ""
    zadania = []

    def __init__(self, login=None, haslo=None):
        self.login = login
        self.haslo = haslo

    def __str__(self):
        return 'User(Imie: {s.imie} | Nazwisko: {s.nazwisko} | Login: {s.login} | Hasło: {s.haslo}'.format(s=self)

    def dodajZadanie(self, zadanie):
        self.zadania.append(zadanie)

