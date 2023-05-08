import json
# tady nemusíme zavřít soubor metoda with soubor automaticky zavře
with open("absolventi.json", encoding="utf-8") as prvni_soubor:
    #data = prvni_soubor.read()
    seznam_absolventu = json.load(prvni_soubor) #načtení už v json formátu

#with open("absolventi.json", encoding="utf-8") as prvni_soubor:
    #data = prvni_soubor.read()
    #seznam_absolventu = prvni_soubor.read # nacte jako řetězec string a ne jako seznam tudíž je těžké k těm datům přistupovat print(type(seznam_absolventu[0]))

#print(data)
print(seznam_absolventu[0])
#print(type(data))
# *print(prvni_soubor.read())
# *tady je třeba nejen otevřít ale i zavřít soubor jinak je soubor dále uzavřený pythonem projakékoliv jiné operace.
#print(open("absolventi.json").read())

import json
hours = {'po': 8, 'ut': 7, 'st': 6, 'ct': 7, 'pa': 8}
with open('hodiny.json', mode='w', encoding='utf-8') as file: #mode r - read, w - write, 
    json.dump(hours, file) #vytvoří soubor hodiny.json v liště VScode

#ukol_1
import json
with open('zavod.json', encoding='utf-8') as file:
    runners = json.load(file)

winner = runners[0]
winner_time = winner["casy"]["oficialni"]

finishers = []
for runner in runners:
    if runner["casy"]["oficialni"] != "DNF":
        finishers.append(runner["jmeno"])

print(finishers)
silver_runner = runners[1]
print(silver_runner)