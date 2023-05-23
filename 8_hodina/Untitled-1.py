# %%
class Kniha:
    def __init__(self, nazev, pocet_stran, cena):
        self.nazev = nazev
        self.pocet_stran = pocet_stran
        self.cena = cena



    def __str__(self) -> str:
        return f"Kniha {self.nazev} má {self.pocet_stran} stran a stojí {self.cena} "
    
    def sleva(self, sleva_na_knihu = 20):
        self.cena = self.cena*((100-20)/100)
        return f"Užij si to :)"
    

Slovnik = Kniha("Tam a tam", 2, 100)
O_detech = Kniha("Zdezde", "5", 200)
Matematika = Kniha("hlehle", "1", 300)


print(Slovnik)
Slovnik.sleva()
print(Slovnik)   


