class Osoba:
    def __init__(self, imie, nazwisko, wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek

    def opisz(self):
        print(f"{self.imie} {self.nazwisko}, {self.wiek} lat.")

class Student(Osoba):
    def __init__(self, imie, nazwisko, wiek, nr_indeksu):
        super().__init__(imie, nazwisko, wiek)
        self.numer_indeksu = nr_indeksu

    def opisz(self):
        print(f"{self.imie} {self.nazwisko}, {self.wiek} lat, {self.numer_indeksu}")


class Pracownik(Osoba):
    def __init__(self, imie, nazwisko, wiek, stanowisko, pensja):
        super().__init__(imie, nazwisko, wiek)
        self.stanowisko = stanowisko
        self.pensja = pensja

    def opisz(self):
         print(f"Opis pracownika {self.imie} {self.nazwisko}, {self.wiek} lat, stanowisko:{self.stanowisko}, wynagrodzenie(pensja):{self.pensja} ")


class PracującyStudent(Student):
    


ktos = Student("Piotr", "Kowalski", 25, 123)
ktos.opisz()
ktos = Pracownik("Piotr", "Kowalski", 25, "mechanik", 5021)
ktos.opisz()