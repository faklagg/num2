# Binaersuche tail rekursiv implementiert
"""
x = Werte
x0 = gesuchter Wert
xstart = Startposition der Suche in Werten
xend = Endposition der Suche in Werten

die Binaersuche ist ein effizienter Algorithmus um einen Wert in einer 
vorsortierten Liste zu finden. Prinzip: Teile und Hersche
Laufzeitkomplexitaet: O(log n)
"""
def binaersucheRekursiv(x, x0, xstart, xend):
    if (xend < xstart): 
        return -1 
    m = (xend + xstart) // 2
    if (x[m] == x0):
        return m 
    elif (x[m] < x0):
        return binaersucheRekursiv(x, x0, m+1, xend)
    else:
        return binaersucheRekursiv(x, x0, xstart, m-1)

def binaersuche(x, x0):
    return binaersucheRekursiv(x, x0, 0, len(x)-1)
