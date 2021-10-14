# NewtonInterpolation
"""
j = Zeilenindex
k = Spaltenindex
x = Stuetzstellen 
fx = zugehoerigen Funktionswerte

die Newtoninterpolation wendet das Verfahren der dividierten Differenzen
auf die uebergebenen Vektoren an. 

Die Stuetzstellen muessen paarweise verschieden sein und die Ableitungen 
koennen nicht mit eingehen. 
Siehe hierzu Hermite Interpolation.

die obere Diagonale des Verfahrens der dividierten Differenzen 
(= Ergnisse im Spaltenvektor fx) sind die 
Koeffizienten a des Polynoms in der Newtonbasis
"""

def NewtonInterpolation(x, fx):
    for k in range(1, len(fx), 1):
        for j in range(len(fx)-1, k-1, -1):
            fx[j] = (fx[j] - fx[j-1]) / (x[j]-x[j-k])
    return fx
