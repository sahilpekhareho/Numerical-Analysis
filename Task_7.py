from math import sqrt, pi, exp
import numpy as np
import matplotlib.pyplot as plt

n_t = {}
for x in range(1, 5):
    for y in range(1, 5):
        for z in range(1, 5):
            if (x**2)+(y**2)+(z**2) not in list(n_t.keys()):
                n_t[(x**2)+(y**2)+(z**2)] = [np.array([x, y, z])]
            else:
                n_t[(x**2)+(y**2)+(z**2)].append(np.array([x, y, z]))


def psibox3D(cardinal, x, y, z, L):
    nx = n_t[cardinal][0][0]
    ny = n_t[cardinal][0][1]
    nz = n_t[cardinal][0][2]
    return (sqrt(8/L**3)) * np.sin(x * nx * pi / L) * np.sin(y * ny * pi / L) * np.sin(z * nz * pi / L)


L = 20
X = np.arange(0, L, 0.01)
Y = np.arange(0, L, 0.01)
Z = np.arange(0, L, 0.01)

resultsx = psibox3D(12, X, Y, Z, L)**2

plt.figure(0)
plt.plot(X, resultsx)