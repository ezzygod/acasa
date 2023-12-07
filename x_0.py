import tkinter as tk  # Importă modulul tkinter pentru a crea interfeța grafică
from tkinter import messagebox  # Importă messagebox din tkinter pentru a afișa ferestre pop-up
import random  # Importă modulul random pentru a genera mutări aleatorii

class JocXsiO:
    def __init__(self, master):
        self.master = master  # Referință către obiectul principal Tk
        self.master.title("X și 0")  # Setează titlul ferestrei

        # Variabila care reține modul de joc: 'Calculator' sau 'Cu altcineva'
        self.mod_joc = tk.StringVar()
        self.mod_joc.set("Calculator")  # Setează implicit modul de joc la 'Calculator'

        # Interfață pentru alegerea modului de joc
        self.creare_interfata_mod_joc()

        # Crearea tablei de joc
        self.creare_tabla()

        # 'X' va începe întotdeauna
        self.jucator_curent = 'X'

    def creare_interfata_mod_joc(self):
        # Eticheta pentru modul de joc
        label_mod_joc = tk.Label(self.master, text="Alege modul de joc:")
        label_mod_joc.grid(row=0, column=0, columnspan=3)

        # Buton pentru alege modul 'Calculator'
        radio_calculator = tk.Radiobutton(self.master, text="Cu Calculatorul", variable=self.mod_joc, value="Calculator")
        radio_calculator.grid(row=1, column=0)

        # Buton pentru alege modul 'Cu altcineva'
        radio_altcineva = tk.Radiobutton(self.master, text="Cu Altcineva", variable=self.mod_joc, value="Altcineva")
        radio_altcineva.grid(row=1, column=1)

    def creare_tabla(self):
        # Crează o matrice pentru tabla de joc
        self.tabla = [[' ' for _ in range(3)] for _ in range(3)]

        # Iterează prin matricea de butoane și le adaugă la interfață
        for i in range(3):
            for j in range(3):
                btn = tk.Button(self.master, text='', font=('normal', 20), width=5, height=2,
                                command=lambda row=i, col=j: self.click_pe_buton(row, col))
                btn.grid(row=i + 2, column=j)  # Adaugă 2 la rând pentru a face loc butoanelor de alegere a modului de joc

    def click_pe_buton(self, row, col):
        # Verifică dacă celula este goală și efectuează mutarea jucătorului curent
        if self.tabla[row][col] == ' ':
            self.tabla[row][col] = self.jucator_curent
            self.actualizare_tabla()
            
            # Verifică dacă jucătorul curent a câștigat
            if self.verifica_castigator(self.jucator_curent):
                messagebox.showinfo("Final joc", f"{self.jucator_curent} a câștigat!")
                self.reinitializare_joc()
            elif self.tabla_plina():
                messagebox.showinfo("Final joc", "Remiză!")
                self.reinitializare_joc()
            else:
                # Schimbă jucătorul curent doar dacă se joacă cu altcineva
                if self.mod_joc.get() == "Altcineva":
                    self.jucator_curent = 'O' if self.jucator_curent == 'X' else 'X'
                else:
                    # Dacă se joacă cu calculatorul, calculează mutarea calculatorului
                    self.calculeaza_mutare_calculator()
                    self.actualizare_tabla()
                    if self.verifica_castigator('O'):
                        messagebox.showinfo("Final joc", "Calculatorul a câștigat!")
                        self.reinitializare_joc()
                    elif self.tabla_plina():
                        messagebox.showinfo("Final joc", "Remiză!")
                        self.reinitializare_joc()

    def actualizare_tabla(self):
        # Actualizează textul butoanelor conform matricei de joc
        for i in range(3):
            for j in range(3):
                text = self.tabla[i][j]
                btn_text = text if text != ' ' else ''
                self.master.grid_slaves(row=i + 2, column=j)[0].config(text=btn_text)

    def verifica_castigator(self, simbol):
        # Verificare pe linii și coloane
        for i in range(3):
            if all(self.tabla[i][j] == simbol for j in range(3)) or \
               all(self.tabla[j][i] == simbol for j in range(3)):
                return True

        # Verificare pe diagonale
        if all(self.tabla[i][i] == simbol for i in range(3)) or \
           all(self.tabla[i][2 - i] == simbol for i in range(3)):
            return True

        return False

    def tabla_plina(self):
        # Verifică dacă tabla este plină
        return all(self.tabla[i][j] != ' ' for i in range(3) for j in range(3))

    def calculeaza_mutare_calculator(self):
        # Calculează mutarea calculatorului în mod aleatoriu
        mutare_disponibila = False
        while not mutare_disponibila:
            rand = random.randint(0, 2)
            coloana = random.randint(0, 2)
            if self.tabla[rand][coloana] == ' ':
                self.tabla[rand][coloana] = 'O'
                mutare_disponibila = True

    def reinitializare_joc(self):
        # Resetează tabla de joc și interfața grafică pentru un nou joc
        for i in range(3):
            for j in range(3):
                self.tabla[i][j] = ' '
                self.master.grid_slaves(row=i + 2, column=j)[0].config(text='')

if __name__ == "__main__":
    try:
        # Creează o instanță a clasei JocXsiO și pornește bucla principală a interfeței grafice
        root = tk.Tk()
        joc = JocXsiO(root)
        root.mainloop()
    except Exception as e:
        print(f"A intervenit o eroare: {e}")

