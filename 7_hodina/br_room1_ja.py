class Balik: #definice třídy by měla začínat velkým písmenem
    
    def __init__(self, adresa, hmotnost,): #konstruktor tridy - specialni metoda
        self.adresa = adresa
        self.hmotnost = hmotnost
        self.doruceno = False
        

    def __str__(self): #specialni metoda
        return f"Balík na adresu: {self.adresa}, o hmotnosti: {self.hmotnost}Kg, byl {'dorucen' if self.doruceno else 'nedorucen'}."
       
    def doruc(self):
        self.doruceno = True
        return f"Balik je dorucen :)"


A1 = Balik("Tam a tam", "2")
A2 = Balik("Zdezde", "5")
B1 = Balik("hlehle", "1")


print(B1)
B1.doruc()
print(B1)