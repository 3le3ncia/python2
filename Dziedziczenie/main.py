from abc import ABC, abstractmethod

class Figura(ABC):
    def __init__(self):
        self._pole = None
        self._obwod = None
    
    @abstractmethod
    def oblicz_pole(self):
        pass
    
    @abstractmethod
    def oblicz_obwod(self):
        pass
    
    def wyswietl_pole(self):
        print(f"Pole: {self.oblicz_pole()}")
    
    def wyswietl_obwod(self):
        print(f"Obwod: {self.oblicz_obwod()}")

class Prostokat(Figura):
    def __init__(self, dlugosc, szerokosc):
        super().__init__()
        self._dlugosc = dlugosc
        self._szerokosc = szerokosc
    
    def oblicz_pole(self):
        return self._dlugosc * self._szerokosc
    
    def oblicz_obwod(self):
        return 2 * (self._dlugosc + self._szerokosc)

class Kolo(Figura):
    def __init__(self, promien):
        super().__init__()
        self._promien = promien
    
    def oblicz_pole(self):
        return 3.14 * self._promien * self._promien
    
    def oblicz_obwod(self):
        return 2 * 3.14 * self._promien

prostokat = Prostokat(4, 6)
prostokat.oblicz_pole()
prostokat.oblicz_obwod()
prostokat.wyswietl_pole()
prostokat.wyswietl_obwod()

kolo = Kolo(3)
kolo.oblicz_pole()
kolo.oblicz_obwod()
kolo.wyswietl_pole()
kolo.wyswietl_obwod()

