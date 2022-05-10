import qutip as qt
import numpy as np

# definition
sx = qt.sigmax(); sy = qt.sigmay(); sz = qt.sigmaz()

# definition
def commutator(x,y):
    return x*y - y*x

# sx*sy = -sy*sx = 1j*sz
print(sx*sy)
print(-sy*sx)
print(1j * sz)

# sy*sz = -sz*sy = 1j*sx
print(sy*sz)
print(-sz*sy)
print(1j*sx)

# sz*sx = -sx*sz = 1j*sy
print(sz*sx)
print(-sx*sz)
print(1j*sy)

# naiseki
print(commutator(0.5*sy,0.5*sz))
print(1j*0.5*sx)