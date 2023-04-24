#Python1 - 3_hodina- (JSON) - ukol 03 - Zuzka Musilová
#ZADÁNÍ:
""" 
Soubor body.json je JSON, který obsahuje informace o získaných bodech z písemky.

Soubor si ulož a načti do slovníku.

Z písemky nebude známka, ale jen Pass/Fail hodnocení neboli prospěl(a)/neprospěl(a). Vytvoř nový slovník. Jeho klíče budou opět jména žáků, a hodnotou bude řetězec "Pass", pokud má jednotlivec alespoň než 60 bodů. Pokud má méně než 60, hodnota bude "Fail".

Výsledný slovník ulož jako JSON do souboru prospech.json.
"""
#ŘEŠENÍ:

import json

#načtení JSON souboru ze zadání do slovníku "testování"
with open('body.json', mode='r', encoding='utf-8') as file:
    testovani = json.load(file)
    #print(testovani)
    #vytvoření nového seznamu se jménem, přiřazení "fail/pass" podle bodů v testu. 
    prosel = {}
    for jmeno, pocet_bodu in testovani.items():
    
        if pocet_bodu >= 60:
            prosel[jmeno] = "pass"
        else:
            prosel[jmeno] = "fail"
    #print(prosel)
#vytvoření nového JSON souboru     
with open('prospech.json', mode='w', encoding='utf-8') as file: #mode r - read, w - write, 
    prospech = json.dump(prosel, file, ensure_ascii=False, indent=2)

#print(prospech)

# Děkuji za kontrolu a přeji hezký den :-)
# Zuzka



