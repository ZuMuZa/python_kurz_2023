from dataclasses import dataclass

@dataclass
class Kniha:
    nazev: str
    stranky: int
    cena: float
    # def __init__(self, nazev, pocet_stran, cena):
    #     self.nazev = nazev
    #     self.stranky = pocet_stran
    #     self.cena = cena

    def sleva(self, o_kolik):
        self.cena *= 1 - (o_kolik / 100)
        #self.cena = self.cena * (1 - (o_kolik / 100))

    def __str__(self) -> str:
        return f"{self.nazev}, {self.stranky} stranek je za {self.cena}"
    
kniha = Kniha("Bajecna leta pod psa", 150, 500)
print(kniha)
kniha.sleva(50)
print(kniha)