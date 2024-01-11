import sys
from ply import lex, yacc
from math import sqrt, log, sin, cos, tan, pow, log10, pi
import tkinter as tk
from tkinter import *

tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'POWER',
    'SQRT',
    'LOG',
    'SIN',
    'COS',
    'TAN',
    'LPAREN',
    'RPAREN',
)

#reguli token
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_POWER = r'\^'
t_SQRT = r'sqrt'
t_LOG = r'log'
t_SIN = r'sin'
t_COS = r'cos'
t_TAN = r'tan'
t_LPAREN = r'\('
t_RPAREN = r'\)'

#regula pentru numere si transformarea nr din sir in obiecte numerice
def t_numar(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t

#ingora spatiile si taburile
t_ignore = ' \t'

#erori neasteptate
def t_error(t):
    print("Caracter incorect",t.value, file=sys.stderr)
    t.lexer.skip(1)
def p_error(t):
    print(f"Eroare de sintaxă la linia {t.lineno}, poziția {t.lexpos}: Caracter necunoscut '{t.value[0]}'", file=sys.stderr)



lexer = lex.lex()

def p_expresii(c):
    '''termen : termen PLUS termen
               | termen MINUS termen
               | termen TIMES termen
               | termen DIVIDE termen
               | termen POWER termen'''
    if c[2] == '+':
        c[0] = c[1] + c[3]
    elif c[2] == '-':
        c[0] = c[1] - c[3]
    elif c[2] == '*':
        c[0] = c[1] * c[3]
    elif c[2] == '/':
        c[0] = c[1] / c[3]
    elif c[2] == '^':
        c[0] = pow(c[1], c[3])

def p_expresii2(p):
    '''expresie : SQRT expresie
                | LOG expresie'''
    if p[1] == 'sqrt':
        p[0] = sqrt(p[2])
    elif p[1] == 'log':
        p[0] = log10(p[2])

def p_expresii3(p):
    '''expresie : SIN expresie
                  | COS expresie
                  | TAN expresie'''
    if p[1] == 'sin':
        p[0] = sin(p[2])
    elif p[1] == 'cos':
        p[0] = cos(p[2])
    elif p[1] == 'tan':
        p[0] = tan(p[2])

def p_expresii4(p):
    'expresie : LPAREN expresie RPAREN'
    p[0] = p[2]

def p_expresii5(p):
    'expresie : NUMBER'
    p[0] = p[1]


# Crearea parser-ului
parser = yacc.yacc()

def expresie_evaluata(expresie):
    rezultat = parser.parse(expresie, lexer=lexer)
    return rezultat

def main():
    if len(sys.argv) != 2:
        print("Utilizare în linia de comandă: python calcfinal.py <expresie_matematică>")
        sys.exit(1)

    expresie = sys.argv[1]
    rezultat = expresie_evaluata(expresie)
    print(f"Rezultatul expresiei '{expresie}' este: {rezultat}")

#PARTEA GRAFICA @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

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
def buton_egal():
    expresie = campInserare.get()
    rezultat = expresie_evaluata(expresie)
    campInserare.delete(0,END)
    campInserare.insert(END,rezultat)

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
