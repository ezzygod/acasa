import sys
from ply import lex, yacc
from math import sqrt, log, sin, cos, tan, pow, log10, pi
import tkinter as tk
# Definirea token-urilor
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

# Reguli de expresie regulate pentru token-uri simple
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

# Regula pentru numere
def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t

# Ignorarea spațiilor albe și a altor caractere nedorite
t_ignore = ' \t'

# Manejarea erorilor
def t_error(t):
    print(f"Caracter neașteptat '{t.value[0]}'", file=sys.stderr)
    t.lexer.skip(1)

# Crearea lexer-ului
lexer = lex.lex()

# Definirea regulilor gramaticii pentru analiza sintactică (yacc)
def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression POWER expression'''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]
    elif p[2] == '^':
        p[0] = pow(p[1], p[3])

def p_expression_unop(p):
    '''expression : SQRT expression
                  | LOG expression'''
    if p[1] == 'sqrt':
        p[0] = sqrt(p[2])
    elif p[1] == 'log':
        p[0] = log10(p[2])

def p_expression_trig(p):
    '''expression : SIN expression
                  | COS expression
                  | TAN expression'''
    if p[1] == 'sin':
        p[0] = sin(p[2])
    elif p[1] == 'cos':
        p[0] = cos(p[2])
    elif p[1] == 'tan':
        p[0] = tan(p[2])

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

def p_error(p):
    print(f"Erroare de sintaxă la '{p.value}'", file=sys.stderr)

# Crearea parser-ului
parser = yacc.yacc()

def evaluate_expression(expression):
    result = parser.parse(expression, lexer=lexer)
    return result

def main():
    if len(sys.argv) != 2:
        print("Utilizare în linia de comandă: python calcfinal.py <expresie_matematică>")
        sys.exit(1)

    expression = sys.argv[1]
    result = evaluate_expression(expression)
    print(f"Rezultatul expresiei '{expression}' este: {result}")

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.expression_entry = tk.Entry(master, width=30)
        self.expression_entry.grid(row=0, column=0, columnspan=4, pady=10)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row_val = 1
        col_val = 0
        for button in buttons:
            tk.Button(master, text=button, width=5, command=lambda b=button: self.button_click(b)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def button_click(self, button):
        current_expression = self.expression_entry.get()
        if button == '=':
            result = evaluate_expression(current_expression)
            self.expression_entry.delete(0, tk.END)
            self.expression_entry.insert(tk.END, str(result))
        else:
            self.expression_entry.insert(tk.END, button)

def main():
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
