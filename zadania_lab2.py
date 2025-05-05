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

#zadanie 4
class PracującyStudent(Student,Pracownik):
    def __init__(self, imie, nazwisko, wiek, numerindeksu, stanowisko, pensja, godziny_pracy):
        Student.__init__(self, imie, nazwisko, wiek, numerindeksu)
        Pracownik.__init__(self, imie, nazwisko, wiek, stanowisko, pensja)
        self.godziny_pracy = godziny_pracy

    def opisz(self):
    #    print((f"Opis pracownika {self.imie} {self.nazwisko}, {self.wiek} lat, numer indeksu:{self.numer_indeksu} ,stanowisko:{self.stanowisko}, wynagrodzenie(pensja):{self.pensja} godziny pracy :{self.godziny_pracy} "))
        Student.opisz(self)
        Pracownik.opisz(self)




# ktos2 = PracującyStudent("Piotr", "Kowalski", 25, 222, "mechanik", 5021, 420)
# ktos2.opisz()

mirek=Student("mirek", "kowalski", 22, 22222)
mirek.opisz()
mirek2=Pracownik("mirek", "kowalski", 22, "qweqwe", 24244)
mirek2.opisz()