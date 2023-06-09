from dataclasses import dataclass

class Zamestnanec:
    def __init__(self, jmeno, pozice):
        self.jmeno = jmeno
        self.pozice = pozice
        self.dovolena = 160

    def cerpej_dovolenou(self, pocet_hodin):
        if self.dovolena >= pocet_hodin:
            self.dovolena -= pocet_hodin
            return "Užij si to."
        else:
            return f"Máš nárok je na {self.dovolena} hodin."

    def __str__(self):
        return f"Zam. {self.jmeno} a pracuje na poz. {self.pozice}"


class Manazer(Zamestnanec):
    def __init__(self, jmeno, pozice, pocet_podrizenych):
        super().__init__(jmeno, pozice)
        self.pocet_podrizenych = pocet_podrizenych

    def __str__(self):
        return super().__str__() + f" - Počet podřízených: {self.pocet_podrizenych}"

@dataclass
class Brigadnik(Zamestnanec):
    jmeno: str
    pozice: str
    uvazek: str
    
    # def __init__(self, jmeno, pozice, uvazek):
    #     super().__init__(jmeno, pozice)
    #     self.uvazek = uvazek

    def __str__(self):
        return super().__str__() + f' velikost uvazku: {self.uvazek}'
    
brigadnik = Brigadnik("jakub", "silak",'polovicni')
print(brigadnik)







