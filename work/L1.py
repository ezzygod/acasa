import math
ip = None


catete = input("Dati valorile catetelor: ")
cateta, cateta2 = map(float, catete.split())

ip = math.sqrt(cateta**2 + cateta2**2)
print("Lungimea ipotenuzei este: ", round(ip, 2))