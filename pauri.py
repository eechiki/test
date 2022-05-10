import qutip as qt
import numpy as np

sx = qt.sigmax(); sy = qt.sigmay(); sz = qt.sigmaz()

def commutator(x,y):
    return x*y - y*x

s0 = qt.Qobj([[1,0],[0,1]])

print(sx*sy)
print(-sy*sx)
print(1j*sz)

print(commutator(0.5*sx, 0.5*sy))
print(1j*0.5*sz)