zapis = """
searchNumber: pavca.czechitas action: search phone number of user dita
user: pavca action: send sms to phone number +420728123456
user: jirka: action: send 2 sms to phone number +420734123456
"""
import re
regularni_vyraz = re.compile(r"(?:\+420)? ?\d{3} ?\d{3} ?\d{3}")
#regularni_vyraz = re.compile(r"\+?\d{12}")
vysledky = regularni_vyraz.findall(zapis)
for vysledek in vysledky:
    print(vysledek)

import re
regularni_vyraz = re.compile(r"(?:\+420)? ?\d{3} ?\d{3} ?\d{3}")
anonymniZapis = regularni_vyraz.sub("X" * 9, zapis)
print(anonymniZapis)