import sys # este un modul standard care oferă funcționalități legate de sistem(path,erori,argumente)
from ply import lex, yacc # lex converteste sir in tokens,iar yacc ia tokens si le face cf. regulilor specificate
from math import sqrt, log, sin, cos, tan, pow, log10, pi # pt folosirea functiilor matematice
import tkinter as tk # interfata grafica
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
    'NEGATE'
)

#reguli tokens
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
t_NEGATE = r'neg'

# regula nr si transformarea lor din sir in nr
def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t

# ignora spatii si taburi
t_ignore = ' \t'

# erori neasteptate
def t_error(t):
    print("Caracter incorect", t.value, file=sys.stderr)
    t.lexer.skip(1)

lexer = lex.lex()

istoric_text = []

def p_expresii(c):
    '''expresie : termen
                | expresie PLUS termen
                | expresie MINUS termen
                | expresie TIMES termen
                | expresie DIVIDE termen
                | expresie POWER termen
                | NEGATE termen'''
    if len(c) == 2:
        c[0] = c[1] # pentru doar un termen
    elif c[2] == '+':
        c[0] = c[1] + c[3]
        istoric_text.append(f"{c[1]} + {c[3]} = {c[0]}")
    elif c[2] == '-':  
        c[0] = c[1] - c[3]
        istoric_text.append(f"{c[1]} - {c[3]} = {c[0]}")
    elif c[2] == '*':
        c[0] = c[1] * c[3]
        istoric_text.append(f"{c[1]} * {c[3]} = {c[0]}")
    elif c[2] == '/':
        c[0] = c[1] / c[3]
        istoric_text.append(f"{c[1]} / {c[3]} = {c[0]}")
    elif c[2] == '^':
        c[0] = pow(c[1], c[3])
        istoric_text.append(f"{c[1]} ^ {c[3]} = {c[0]}")
    elif c[1] == 'neg':
        c[0] = -c[2]
        istoric_text.append(f"neg{c[1]} = {c[0]}")

def p_termen(c):
    '''termen : termen TIMES factor
              | termen DIVIDE factor
              | factor'''
    if len(c) == 2:
        c[0] = c[1]
    elif c[2] == '*':
        c[0] = c[1] * c[3]
    elif c[2] == '/':
        c[0] = c[1] / c[3]

def p_factor(c):
    '''factor : NUMBER
              | SQRT factor
              | LOG factor
              | SIN factor
              | COS factor
              | TAN factor
              | LPAREN expresie RPAREN'''
    if len(c) == 2:
        c[0] = c[1]
    elif c[1] == 'sqrt':
        c[0] = sqrt(c[2])
        istoric_text.append(f"sqrt({c[2]}) = {c[0]}")
    elif c[1] == 'log':
        c[0] = log10(c[2])
        istoric_text.append(f"log({c[2]}) = {c[0]}")
    elif c[1] == 'sin':
        c[0] = sin(c[2])
        istoric_text.append(f"sin({c[2]}) = {c[0]}")
    elif c[1] == 'cos':
        c[0] = cos(c[2])
        istoric_text.append(f"cos({c[2]}) = {c[0]}")
    elif c[1] == 'tan':
        c[0] = tan(c[2])
        istoric_text.append(f"tan({c[2]}) = {c[0]}")
    elif c[1] == '(':
        c[0] = c[2]

# parser creat (aplica regulile definite pentru efectuarea operatiunilor specifice definite)
parser = yacc.yacc()

def evaluare_expresie(expresie):
    rezultat = parser.parse(expresie)
    return rezultat


# PARTEA GRAFICĂ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

calculator = Tk()
calculator.title("Calculator")

butoane = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '', '+',
    'log', 'sin', 'cos', 'tan',
]
procent = '%'
clear = 'C'
paranteza_deschisa = '('
paranteza_inchisa = ')'
radical = 'sqrt'
putere = '^'
negare = 'neg'


campInserare = Entry(calculator, width=25)
campInserare.grid(row=0, column=0, columnspan=4, pady=10)

#PARTEA DE ISTORIC AFISARE
istoric = Listbox(calculator, width=35, height=6)
istoric.grid(row=7, column=0, columnspan=5, pady=10)

#gestionam evenimente cu butoane
def buton_egal():
    expresie = campInserare.get()
    rezultat = evaluare_expresie(expresie)
    campInserare.delete(0, END)
    campInserare.insert(END, rezultat)

    #istoricu
    istoric_text.append(f"{expresie} = {rezultat}")
    istoric.insert(END, f"{expresie} = {rezultat}")

def buton_click(valoare):
    text_curent = campInserare.get()
    campInserare.delete(0, END)
    campInserare.insert(END, text_curent + valoare)

def buton_del():
    text_curent = campInserare.get()
    campInserare.delete(len(text_curent) - 1)

def buton_clear():
    campInserare.delete(0, 'end')

def clear_istoric():
    istoric.delete(0, END)
    istoric_text.clear()    

row_val = 2
col_val = 0

# Inserare butoane
for buton in butoane:
    Button(calculator, text=buton, width=5, height=2, command=lambda b=buton: buton_click(b)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

row_val = 1
col_val = 4

# buton delete
Button(calculator, text="Del", width=5, height=2, command=buton_del).grid(row=1, column=4)
# buton %
Button(calculator, text="^", width=5, height=2, command=lambda b=putere: buton_click(b)).grid(row=1, column=0)
# buton C
Button(calculator, text="C", width=5, height=2, command=buton_clear).grid(row=1, column=1)
# paranteza deschisa/inchisa
Button(calculator, text="(", width=5, height=2, command=lambda b=paranteza_deschisa: buton_click(b)).grid(row=1, column=2)
Button(calculator, text=")", width=5, height=2, command=lambda b=paranteza_inchisa: buton_click(b)).grid(row=1, column=3)
# butonu de egal
Button(calculator, text="=", width=5, height=2, command=buton_egal).grid(row=5, column=2)
# buton radical si pow
Button(calculator, text="sqrt", width=5, height=2, command=lambda b=radical: buton_click(b)).grid(row=2, column=4)
# buton stergere istoric
Button(calculator, text="Cist", width=5, height=2, command=clear_istoric).grid(row=4, column=4)
#buton negare numar
Button(calculator, text="neg", width=5, height=2, command=lambda b=negare: buton_click(b)).grid(row=3, column=4)

calculator.geometry("220x400")  
calculator.mainloop()
