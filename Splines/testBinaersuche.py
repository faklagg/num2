import numpy as np 
from binaersuche import binaersuche as binaer

x = np.linspace(1,25,25)
print(x)
such = 23

# ternary operator
if (binaer(x, such) != -1):
    print("Wert " + str(such) + " gefunden an Position " 
        + str(binaer(x, such))) 
else:
    print("Wert " + str(such) + " nicht gefunden" )
