import sys
from ply import lex, yacc
from math import sqrt, log10, sin, cos, tan, pow, pi

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
tPlus = r'\+'
tMinus = r'-'
tInmultire = r'\*'
tImpartire = r'/'
tPutere = r'\*\*'
tRadical = r'sqrt'
tLogaritm = r'log'
tSinus = r'sin'
tCosinus = r'cos'
tTangenta = r'tan'
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
def p_expression_unop(p):
    '''expression : SQRT expression
                  | LOG10 expression'''
    if p[1] == 'sqrt':
        p[0] = sqrt(p[2])
    elif p[1] == 'log10':
        p[0] = log10(p[2])

# Crearea parser-ului
parser = yacc.yacc()

def evaluate_expression(expression):
    result = parser.parse(expression, lexer=lexer)
    return result

def main():
    if len(sys.argv) != 2:
        print("Utilizare în linia de comandă: python calculator.py <expresie_matematică>")
        sys.exit(1)

    expression = sys.argv[1]
    result = evaluate_expression(expression)
    print(f"Rezultatul expresiei '{expression}' este: {result}")

if __name__ == "__main__":
    main()
