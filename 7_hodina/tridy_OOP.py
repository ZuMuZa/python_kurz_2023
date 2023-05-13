# zaměstnanec: jmeno, pozici
"""
frantisek = ["Frantisek Novak", "ucetni"]
alena =["Alena Drobna", "sefova"]

print(frantisek[1])


frantisek={"jmeno": "Frantisek Novak", "pozice": "ucetni"}
alena={"jmeno": "Alena Drobna", "pozice": "sefova"}

zamestnanci = [frantisek, alena]
"""
"""
class Zamestnanec: #definice třídy by měla začínat velkým písmenem
    jmeno = ""
    pozice = ""

    

frantisek = Zamestnanec() #objekt
frantisek.jmeno = "Frantisek Novak"
frantisek.pozice = "ucetni"

print(frantisek.pozice)

alena = Zamestnanec() #objekt
alena.jmeno = "Alena Drobna"
alena.pozice = "sefova"

print(alena.pozice)
"""

class Zamestnanec: #definice třídy by měla začínat velkým písmenem
    
    def __init__(self, jmeno, pozice, sickday = 3,): #konstruktor tridy - specialni metoda
        self.atribut_jmeno = jmeno
        self.atribut_pozice = pozice
        self.pocet_dni_dovolene = 25   #lze definovat i mimo konstruktor tridy
        self.sickday = sickday
        #self je smerovano na konkretního zamestnance

    def __str__(self): #specialni metoda
        return f"Zamestnanec {self.atribut_jmeno} pracuje na pozici {self.atribut_pozice}"
    
    def info(self): #metoda tridy
        return f"Zamestnanec {self.atribut_jmeno} pracuje na pozici {self.atribut_pozice}"
    
    def cerpani_dovolene(self, days):
        if self.pocet_dni_dovolene >= days:
            #self.pocet_dni_dovolene = self.pocet_dni_dovolene - days   # zjednodušený zápis níže
            self.pocet_dni_dovolene -= days
            return f"Užij si to :)"
        else:
            return f"Bohužel máš narok jen na {self.pocet_dni_dovolene} dní."

frantisek = Zamestnanec("Frantisek Novak", "ucetni") #objekt  pri vytvareni se nam zavola __init__
alena = Zamestnanec("Alena Drobna", "sefova")

zamestnanci = [frantisek, alena]
print(frantisek.atribut_jmeno)
print(alena.atribut_jmeno)

print(frantisek) # hezky vypíše ta metoda str proteže bez ní by to vypisovalo osklivý zápis s adresou v hexa....kdežto tady to je hezky -> print(str(frantisek))
print(frantisek.sickday)
print(frantisek.info())

print(frantisek.cerpani_dovolene(5))
print(frantisek.pocet_dni_dovolene)
print(frantisek.cerpani_dovolene(10))
print(frantisek.pocet_dni_dovolene)
print(frantisek.cerpani_dovolene(15))
print(frantisek.pocet_dni_dovolene)