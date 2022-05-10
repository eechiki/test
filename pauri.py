import qutip as qt
import numpy as np

# definition
sx = qt.sigmax(); sy = qt.sigmay(); sz = qt.sigmaz()
s0 = qt.Qobj([[1,0],[0,1]])

# definition
def commutator(x,y):
    return x*y - y*x

# sx*sy = -sy*sx = 1j*sz
print(sx*sy)
print(-sy*sx)
print(1j*sz)

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

# naiseki
print(commutator(0.5*sy,0.5*sz))
print(1j*0.5*sx)

# naiseki
print(commutator(0.5*sz,0.5*sx))
print(1j*0.5*sy)

# exp alpha = 1
# sahen
print((1j*1*sx).expm())

# uhen
print(np.cos(1)*s0+1j*np.sin(1)*sx)

# exp alpha = 0,(1/3)pi,(2/3)pi,pi,(4/3)pi,(5/3)pi

for i in range(0,6):
    alpha = (np.pi/3.0)*i
    LS = (1j*alpha*sx).expm()
    RS = s0*np.cos(alpha) + 1j*sx*np.sin(alpha)
    print("alpha=",alpha,"\n","(左辺)",LS,"\n","(右辺)",RS)
    print("\n")














