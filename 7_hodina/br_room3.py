class Zamestnanec: #definice třídy by měla začínat velkým písmenem
    
    def __init__(self, jmeno, pozice): #konstruktor tridy - specialni metoda
        self.jmeno = jmeno
        self.pozice = pozice
        
    def __str__(self): #specialni metoda
        return f"Zamestnanec {self.jmeno} pracuje na pozici {self.pozice}"
    
class Brigadnik(Zamestnanec, ):
    
    def __init__(self, jmeno, pozice, uvazek): 
        super().__init__(jmeno, pozice)  
        self.uvazek = uvazek
            
    def __str__(self):
        return f"{super().__str__()} a má úvazek o velikosti {self.uvazek} oproti plnému úvazku."
    

frantisek = Zamestnanec("frantisek", "ucetni")
alena = Brigadnik(jmeno="Alena", pozice="vedouci vsech ucetni", uvazek=3/4)
print(alena)
print(alena.jmeno)
print(alena.uvazek)
#alena.pridej_podrizeneho(frantisek)
#print(alena.vypis_podrizene())

