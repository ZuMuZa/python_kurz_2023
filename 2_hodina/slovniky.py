pekarna = {
    "houska": 20,
    "rohlik": 5,
    "chleba": 40,
    "loupak": 20,
}

produkty = ["houska", "rohlik", "chleba", "loupak"]
#klic je unikátní u pekárny je to produkt

print(pekarna)
print(pekarna["chleba"])

klic = "rohlik"
print(f"Klic: (klic), hodnota: {pekarna[klic]} korun.")
print("Klic: " + klic + ", hodnota:" + str(pekarna[klic]) + "korun.")

#výpis hodnota
produkt = input("Zadej produkt: ")
print(f"{produkt} stojí {pekarna[klic]} korun.")

if produkt in pekarna: #produkt je v pekárně ...klic je ve slovníku (to jsou hesla v anglicko českém slovniku)
    print(f"{produkt} stojí {pekarna[produkt]} korun.")
else: #produkt není v pekárně
    print(f"bohužel, produkt {produkt} neprodáváme.")

#přidávání do slovniku
pekarna["zakusek"] = 35
print(pekarna)

#odebírání do slovníku
cena_houska = pekarna.pop("houska")
print(pekarna)
print(cena_houska)


# slovník s více
#pekarna = {
#    (houska, bílá): 10,
#    (houska, celozrna): 15,
#}