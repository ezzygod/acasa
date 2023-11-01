text = input("Introduceti text: ")
majuscule =""
vocale = ""

for caracter in text:
    if caracter.lower() in "aeiou":
        majuscule += caracter.upper()
    else:
        majuscule += caracter

print(majuscule)
        

