class Balik: #definice třídy by měla začínat velkým písmenem
    
    def __init__(self, adresa, hmotnost,): #konstruktor tridy - specialni metoda
        self.adresa = adresa
        self.hmotnost = hmotnost
        self.doruceno = False
        

    def __str__(self): #specialni metoda
        return f"Balík na adresu: {self.adresa}, o hmotnosti: {self.hmotnost}Kg, byl {'dorucen' if self.doruceno else 'nedorucen'}"
       
    def doruc(self):
        self.doruceno = True
        return f"Balik je dorucen :)"
    
class CennyBalik(Balik):
    def __init__(self, adresa, hmotnost, hodnota): #konstruktor tridy - specialni metoda
        #Zamestnanec.__init__(self,jmeno, pozice) bud takto u případu kdy Manazer dědí z více tříd nebo *****
        super().__init__(adresa, hmotnost)  #takto *****
        self.hodnota = hodnota
        
    
    def __str__(self):
        return f"{super().__str__()} a má cenu {self.hodnota} Kč."    


A1 = Balik("Tam a tam", "2")
A2 = Balik("Zdezde", "5")
B1 = CennyBalik("hlehle", "1", 200)


print(A1)
B1.doruc()
print(B1)