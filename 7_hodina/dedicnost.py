
class Zamestnanec: #definice třídy by měla začínat velkým písmenem
    
    def __init__(self, jmeno, pozice): #konstruktor tridy - specialni metoda
        self.jmeno = jmeno
        self.pozice = pozice
        
    def __str__(self): #specialni metoda
        return f"Zamestnanec {self.jmeno} pracuje na pozici {self.pozice}"
    
class Manazer(Zamestnanec, ): #Manažer dědí od zamestnance - manazer přebírá atributy a metody zamestnance lze přidat druhou třídu dědičnosti """Druha_trida"""
    
    def __init__(self, jmeno, pozice, pocet_podrizenych): #konstruktor tridy - specialni metoda
        #Zamestnanec.__init__(self,jmeno, pozice) bud takto u případu kdy Manazer dědí z více tříd nebo *****
        super().__init__(jmeno, pozice)  #takto *****
        self.pocet_podrizenych =pocet_podrizenych
        self.podrizeni = []
    
    def __str__(self):
        return f"{super().__str__()} a má tým o velikosti {self.pocet_podrizenych} podřízených"
    
    def pridej_podrizeneho(self, novy_podrizeny):
        self.podrizeni.append(novy_podrizeny)

    def vypis_podrizene(self):
        podrizeni = ""
        for person in self.podrizeni:
            podrizeni += person.jmeno + ", "
            return podrizeni



frantisek = Zamestnanec("frantisek", "ucetni")
alena = Manazer(jmeno="Alena", pozice="vedouci vsech ucetni", pocet_podrizenych=3)
print(alena)
print(alena.jmeno)
print(alena.pocet_podrizenych)
alena.pridej_podrizeneho(frantisek)
print(alena.vypis_podrizene())
"""

class Zamestnanec: #definice třídy by měla začínat velkým písmenem
    
    def __init__(self, jmeno, pozice): #konstruktor tridy - specialni metoda
        self.jmeno = jmeno
        self.pozice = pozice
        
    def __str__(self): #specialni metoda
        return f"Zamestnanec {self.jmeno} pracuje na pozici {self.pozice}"
    
class Manazer(Zamestnanec, ): #Manažer dědí od zamestnance - manazer přebírá atributy a metody zamestnance
    
    def __init__(self, jmeno, pocet_podrizenych): #konstruktor tridy - specialni metoda
        #Zamestnanec.__init__(self,jmeno,) bud takto u případu kdy Manazer dědí z více tříd nebo *****
        super().__init__(jmeno, pozice = "manazer")  #takto *****
        self.pocet_podrizenych =pocet_podrizenych
    
    def __str__(self):
        return f"{super().__str__()} a má tým o velikosti {self.pocet_podrizenych} podřízených"
    

alena = Manazer(jmeno="Alena", pocet_podrizenych=3)
print(alena)
print(alena.jmeno)
print(alena.pocet_podrizenych)
print(alena.pozice)
"""
