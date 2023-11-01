text = input("Introduceti un text: ")
consoane = ""
vocale = ""

for caracter in text:
    if caracter.isalpha and caracter.lower() not in "aeiou":
        consoane += caracter

for caracter2 in text:
    if caracter2.isalpha and caracter2.lower() in"aeiou":
        vocale += caracter2

print(consoane)
print(vocale)
