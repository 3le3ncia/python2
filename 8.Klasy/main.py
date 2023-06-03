class Czytelnik:
    def __init__(self, imie: str, nazwisko: str, nr_telefonu: str, email: str, ksiazka: str):
        self.imie = imie
        self.nazwisko = nazwisko
        self.nr_telefonu = nr_telefonu
        self.email = email
        self.ksiazka = ksiazka

    def __str__(self):
        return f"{self.imie} {self.nazwisko}, tel: {self.nr_telefonu}, email: {self.email}, ksiazka: {self.ksiazka}"
czytelnik1 = Czytelnik('Julia', 'Pietrak', '321321321', 'valorantlover@gmail.com', "Zrodzenie z legendy")
czytelnik2 = Czytelnik("Joanna", "Jendrych", "987899878", "shakewaniliowy@mcdonald.com", "Szklany tron")