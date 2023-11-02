
hat = []

while True:
    actiune = input("Introduceti 'adauga' sau 'elimina' pentru a modifica lista cu obiecte sau 'iesire' pentru a incheia: ").lower()

    if actiune == 'adauga':
        numar = int(input("Introduceti un numar pe care doriti sa-l adaugati in lista cu obiecte: "))
        hat.append(numar)
    elif actiune == 'elimina':
        if len(hat) == 0:
            print("Lista cu obiecte este goala. Nu se poate elimina niciun numar.")
        else:
            numar_eliminat = hat.pop()
            print(f"A fost eliminat numarul {numar_eliminat} din lista cu obiecte.")
    elif actiune == 'iesire':
        break
    else:
        print("Intrare invalida. Va rugam sa introduceti 'adauga', 'elimina' sau 'iesire'.")

print("Continutul listei cu obiecte este:", hat)