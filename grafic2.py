import sys
from ply import lex, yacc
from math import sqrt, log, sin, cos, tan, pow, log10, pi
import tkinter as tk
from tkinter import *

calculator = Tk()
calculator.title("Calculator")

butoane = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'log','sin','cos','tan',
    ]
procent = '%'
clear = 'C'
paranteza_deschisa = '('
paranteza_inchisa = ')'

campInserare = Entry(calculator)
campInserare.grid(row=0, column=0, columnspan=4, pady=10)

# Functii pentru gestionarea evenimentelor de apasare a butoanelor
def buton_click(valoare):
    textcurent = campInserare.get()
    campInserare.delete(0, END)
    campInserare.insert(END, textcurent + valoare)

def buton_del():
    textcurent = campInserare.get()
    campInserare.delete(len(textcurent) - 1)

def buton_clear():
    campInserare.delete(0,'end')


row_val = 1
col_val = 0

#inserare butoane
for buton in butoane:
    Button(calculator, text=buton, width=5, height=2, command=lambda b=buton: buton_click(b)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

row_val = 1
col_val = 4


#buton delete
Button(calculator, text="Del", width=5, height=2, command=buton_del).grid(row=1, column=4)
#buton %
Button(calculator, text="%", width=5, height=2, command=lambda b=procent: buton_click(b)).grid(row=5, column=4)
#buton C
Button(calculator, text="C", width=5, height=2, command=buton_clear).grid(row=2, column=4)
#paranteza deschisa/inchisa
Button(calculator, text="(", width=5, height=2, command=lambda b=paranteza_deschisa: buton_click(b)).grid(row=3, column=4)
Button(calculator, text=")", width=5, height=2, command=lambda b=paranteza_inchisa: buton_click(b)).grid(row=4, column=4)

calculator.geometry("225x240")

calculator.mainloop()