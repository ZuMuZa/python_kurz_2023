import re
regularni_vyraz = re.compile(r"\d{9,10}")

rezetec = "9511121234"
print(regularni_vyraz.match(rezetec))
rezetec = "ahoj"
print(regularni_vyraz.match(rezetec))