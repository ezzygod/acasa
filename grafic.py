import sys
from ply import lex, yacc
from math import sqrt, log, sin, cos, tan, pow, log10, pi
import tkinter as tk
from tkinter import *

token = ('NUMBER', 'PLUS', 'MINUS', 'INMULTIRE', 'IMPARTIRE', 'PUTERE', 'RADICAL', 'LOG', 'SIN', 'COS', 'TAN', 'LPAREN', 'RPAREN')

#reguli token
t_PLUS = r'\+'
t_MINUS = r'-'
t_INMULTIRE = r'\*'
t_IMPARTIRE = r'/'
t_PUTERE = r'\^'
t_RADICAL = r'sqrt'
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


lexer = lex.lex()

def p_expresii(c):
    '''termen : termen PLUS termen
                    | termen MINUS termen
                    | termen INMULTIRE termen
                    | termen IMPARTIRE termen
                    | termen PUTERE termen'''
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


#PARTEA GRAFICA @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@




calculator = Tk()
calculator.title("Calculator")

butoane = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]


campInserare = Entry(calculator)
campInserare.grid(row=0, column=0, columnspan=4, pady=10)

# Funcția pentru gestionarea evenimentelor de apăsare a butoanelor
def buton_click(valoare):
    textcurent = campInserare.get()
    campInserare.delete(0, END)
    campInserare.insert(END, textcurent + valoare)

def buton_del():
    textcurent = campInserare.get()
    campInserare.delete(len(textcurent) - 1)


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

calculator.geometry("225x200")

calculator.mainloop()
