# class Osoba:
#     def __init__(self, blabla, nazwisko, rok_urodzenia):
#         self.imie = blabla
#         self.nazwisko = nazwisko
#         self.rok_urodzenia = rok_urodzenia
#     def oblicz_wiek(self, rok_biezacy):
#         return rok_biezacy - self.rok_urodzenia
#     def przedstaw_sie(self):
#         print(f"Jestem {self.imie} {self.nazwisko}, urodzony/a w {self.rok_urodzenia} roku.")
# ############### Koniec klasy ####################################
# # Utworzenie obiektu klasy Osoba
# ja = Osoba("Jan", "Kowalski", 1975)
# # Wywołanie metody przedstaw_sie
# ja.przedstaw_sie()
# # Wywołanie metody oblicz_wiek
# # wiek = ja.oblicz_wiek(2024)
# # print(f"Mam {wiek} lat.")
# kolega_1 = Osoba("Maciej", "Maliniak", 2002)
# kolega_1.przedstaw_sie()

# kolega_2 = Osoba(2003, "Maliniak", 2002)
# kolega_2.przedstaw_sie()


# class Ptak:
#  def __init__(self, gatunek,typ):
#     self.gatunek=gatunek
#     self.typ=typ
# wrona = Ptak('Wrona',"drapieżnik")
# kruk = Ptak('Kruk',"drapieżnik")
# # wrona.typ = Ptak ('drapieżnik')
# print(f'Wrona jest ptakiem typu {wrona.typ}')
# print(f'Kruk jest ptakiem typu {kruk.typ}')


class Samochod:
    def __init__(self, marka, model, rocznik):
        self.__marka = marka
        self.__model = model
        self.__rocznik = rocznik

    def get_marka(self):
        return self.__marka
    
    def set_marka(self, nowa_marka):
        self.__marka = nowa_marka
        
    def set_rocznik(self, nowy_rocznik):
        if int(nowy_rocznik)>1980:
            self.__rocznik = nowy_rocznik
        else:
            print('rocznik musi byc wiekszy niż 1980')

    def opisz(self):
        return f"To jest samochód marki {self.__marka} model {self.__model}."


skoda = Samochod("skoda",'felicja',2000)
print(skoda.get_marka())
print('podaj nowy rocznik')
skoda.set_rocznik(input())
