# imports
import numpy as np
import matplotlib.pyplot as plt
from AitkenNeville import AitkenNeville as aitken

# vars
n = 12 
f = lambda x: 1/(x**2+1)
x = np.linspace(-5, 5, n)
fx = f(x)
s = np.linspace(x[0], x[-1], 10*n)


ps = np.zeros(len(s))
for j in range(0, len(s)-1, 1):
    ps[j] = aitken(x, f(x), s[j])

#print(x)
#print(fx)
#print(s)
#print(ps)

fig, ax = plt.subplots()
ax.plot(x, fx)
ax.plot(s, ps)
ax.set(xlabel='x', ylabel='fx', title='Polynominterpolation mit AitkenNeville')
ax.grid()
plt.show()
