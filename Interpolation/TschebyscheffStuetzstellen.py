# TschebyscheffStuetzstellen
"""
a = linke Intervallgrenze
b = rechte Intervallgrenze
n = Anzahl der Stuetzstellen
Berechnung der Stuetzstellen nach Tschebyscheff um den Interpolationsfehler
der Polynominterpolation zu minimieren. 
Ablauf: 
1. Stuetzstellen auf Intervall mit Tschebyscheff bestimmen
2. zugehörige Funktionswerte ermitteln
3. Polynom interpolieren
Vorteile: Polynome sind mathematisch einfach handhabbar
"""

# imports
import math
def TschebyscheffStuetzstellen(a, b, n):
    tk = [0]*n
    xk = [0]*n
    for k in range(0, n, 1):
        # print(k)
        # math.cos rechnet mit rad 
        #tk liegt als Knotenvektor mit Werten zwischen -1 und 1 vor
        tk[k] = math.cos(math.pi*((2*k+1)/(2*(n-1)+2)))
        xk[k] = ((a+b)/2) + ((b-a)/2)*tk[k]
    #[::-1] extended slicing um liste umzudrehen/flippen
    return xk[::-1]

