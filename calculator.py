import sys
from sympy import sympify, sqrt, log, sin, cos, tan, log, symbols

def evaluate_expresie(expresie):
    x, y, z = symbols('x y z')  # Define variabilele simbolice

    try:
        rezultat = sympify(expresie).evalf(subs={x: 1, y: 2, z: 3})
        return rezultat
    except Exception as e:
        return f"Eroare: {e}"

def main():
    if len(sys.argv) != 2:
        print("Usage: python calculator.py <expresie_matematica>")
        sys.exit(1)

    expresie = sys.argv[1]
    rezultat = evaluate_expresie(expresie)
    print(f"Rezultatul expresiei '{expresie}' este: {rezultat}")

if __name__ == "__main__":
    main()