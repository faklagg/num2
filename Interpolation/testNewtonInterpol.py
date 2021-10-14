import numpy as np
from NewtonInterpolation import NewtonInterpolation as ni
from HornerNewton import HornerNewton as hn

x = np.linspace(0,2,3)
f = lambda x: x**2
fx = f(x)

"""
print("x\t=\t" + str(x))
print("fx\t=\t" + str(fx))
print("f(x)\t=\t" + str(f(x)))
"""

a = ni(x, fx)
print("a = " + str(a))

erg = hn(a,2,x)
print("erg = " + str(erg))
