class Czytelnik:
    def __init__(self, imie: str, nazwisko: str, nr_telefonu: str, email: str, ksiazka: str):
        self.__imie = imie
        self.__nazwisko = nazwisko
        self.__nr_telefonu = nr_telefonu
        self.__email = email
        self.__ksiazka = ksiazka

    def __str__(self):
        return f"{self.__imie} {self.__nazwisko}, tel: {self.__nr_telefonu}, email: {self.__email}, ksiazka: {self.__ksiazka}"