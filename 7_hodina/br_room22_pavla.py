from dataclasses import dataclass

@dataclass
class Zamestnanec:
    jmeno: str
    pozice: str
    zkusebni_doba: bool
    # def __init__(self, jmeno, pozice, zkusebni_doba):
    #     self.jmeno = jmeno
    #     self.pozice = pozice
    #     self.zkusebni_doba = zkusebni_doba

    def __str__(self):
        return f"{self.jmeno} pracuje na pozici {self.pozice}." \
               f"{' Je ve zkušební době.' if self.zkusebni_doba else ''}"


zam1 = Zamestnanec('Jarolim', 'svarec', False)
print(zam1)

zam2 = Zamestnanec('Jaroslava', 'programator', True)
print(zam2)