def afisare_tabel(tabel):
    for linie in tabel:
        print("|".join(linie))
        print("-----")

def verificare_castigator(tabel, simbol):
    # Verificăm liniile, coloanele și diagonalele pentru un câștigător
    for i in range(3):
        if tabel[i][0] == tabel[i][1] == tabel[i][2] == simbol:
            return True
        if tabel[0][i] == tabel[1][i] == tabel[2][i] == simbol:
            return True
    if tabel[0][0] == tabel[1][1] == tabel[2][2] == simbol:
        return True
    if tabel[0][2] == tabel[1][1] == tabel[2][0] == simbol:
        return True
    return False

tabel = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]  # Inițializăm tabela

toate_pozitiile = list(range(1, 10))  # Lista tuturor pozițiilor disponibile
castigator = None

while toate_pozitiile:
    afisare_tabel(tabel)

    # Jucătorul cu X
    pozitia1 = int(input("Jucătorul cu X introduce poziția (1-9) pe care vrea să o ocupe: "))
    if pozitia1 < 1 or pozitia1 > 9 or tabel[(pozitia1 - 1) // 3][(pozitia1 - 1) % 3] != " ":
        print("Mișcare invalidă. Reîncercați.")
        continue
    tabel[(pozitia1 - 1) // 3][(pozitia1 - 1) % 3] = "X"
    toate_pozitiile.remove(pozitia1)
    
    afisare_tabel(tabel)

    # Verificăm câștigătorul pentru X
    if verificare_castigator(tabel, "X"):
        castigator = "X"
        break

    if not toate_pozitiile:
        break

    # Jucătorul cu O
    pozitia2 = int(input("Jucătorul cu O introduce poziția (1-9) pe care vrea să o ocupe: "))
    if pozitia2 < 1 or pozitia2 > 9 or tabel[(pozitia2 - 1) // 3][(pozitia2 - 1) % 3] != " ":
        print("Mișcare invalidă. Reîncercați.")
        continue
    tabel[(pozitia2 - 1) // 3][(pozitia2 - 1) % 3] = "O"
    toate_pozitiile.remove(pozitia2)

    # Verificăm câștigătorul pentru O
    if verificare_castigator(tabel, "O"):
        castigator = "O"
        break

if castigator:
    afisare_tabel(tabel)
    print(f"Câștigătorul este jucătorul cu {castigator}.")
else:
    afisare_tabel(tabel)
    print("Remiză! Jocul s-a încheiat fără câștigător.")
