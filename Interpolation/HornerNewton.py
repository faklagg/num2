# HornerNewton
"""
a = Koeffizientenvektor des Newtonpolynoms
x0 = Auswertestelle
x = Vektor der Stuetzstellen

Hornerschema ist effizientes Schema (Aufwand O(n) = linearer Aufwand) 
zum Auswerten des Newtonpolynoms bei bekannten Koeffizienten a
"""

def HornerNewton(a, x0, x):
    dfx = 0
    fx = a[-1]
    # Achtung Indizes von Range! -1 an zweiter Stelle notwendig, damit bis 
    # 0 gezaehlt wird!
    for i in range(len(a)-2, -1, -1):
        dfx = fx + (x0-x[i])*dfx
        fx = a[i] + fx*(x0-x[i])
    return [fx, dfx]
