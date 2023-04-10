school_report = {
    "Český jazyk": 1,
    "Anglický jazyk": 1,
    "Matematika": 1,
    "Přírodopis": 2,
    "Dějepis": 1,
    "Fyzika": 2,
    "Hudební výchova": 4,
    "Výtvarná výchova": 2,
    "Tělesná výchova": 3,
    "Chemie": 4,
}

#průměrná známka
print(sum(school_report.values())/len(school_report))

# vypiš předměty se známkou 1
print(school_report.items())


print(f"Předměty se známkou 1: ")
for predmet, znamka in school_report.items():
    if znamka == 1:
        print(predmet)
   




books = [
    {"title": "Vražda s příliš mnoha notami", "pages": 450, "rating": 5},
    {"title": "Vražda podle knihy", "pages": 524, "rating": 9},
    {"title": "Past", "pages": 390, "rating": 4},
    {"title": "Popel popelu", "pages": 411, "rating": 10},
    {"title": "Noc, která mě zabila", "pages": 159, "rating": 7},
    {"title": "Vražda, kouř a stíny", "pages": 258, "rating": 6},
    {"title": "Zločinný steh", "pages": 542, "rating": 8},
    {"title": "Zkus mě chytit", "pages": 247, "rating": 7},
    {"title": "Vrah zavolá v deset", "pages": 396, "rating": 6},
]

print(books[0]["pages"])
pocet_stran = 0
for kniha in books:
    pocet_stran += kniha["pages"]
    #stejný jako pocet_stran = pocet_stranek + kniha["pages"]
print(f"celkem precetl: {pocet_stran} stranek.")

#alternativní řešení přes list komprehension
#print(f"soucet přeslist compreh: {sum([kniha["pages"] for kniha in books])}")

#pripis do programu výpočet počtu knih, kterým dal Gustav hodnocení alespoŇ 8.
pocet_nad_osm = 0
for kniha in books:
    if kniha["rating"] >= 8:
        pocet_nad_osm += 1
print(f"pocet knih s hodnocením nad osm je: {pocet_nad_osm}")
