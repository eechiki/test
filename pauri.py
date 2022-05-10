import qutip as qt
import numpy as np

sx = qt.sigmax(); sy = qt.sigmay(); sz = qt.sigmaz()

def commutator(x,y):
    return x*y - y*x

print(sx*sy)