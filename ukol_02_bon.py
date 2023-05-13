morse_code = {
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-",
}

text_pro_prevod = str(input ("Zadej textový řetězec pro převod do Morseovy abecedy: "))

print(text_pro_prevod[1])

seznam_znaku = list(text_pro_prevod)
print(seznam_znaku)
item = {"abeceda": "0", "preklad": "-----"}
znak = {"znak": seznam_znaku}
morse = []
For znak in seznam_znaku:
    #najdi ke každému x (ze zadaneho textu) znak z morse_code, vytvoř nový textový řetězec.
    #names.add("")
    if znak in morse_code:
       morse = morse + morse_code[znak]  
    else:
        morse = morse + " "
print(morse)
 """