from math import sqrt, pi, factorial, exp
import numpy as np
import matplotlib.pyplot as plt
from scipy import special as scp

k = 2
kappa = 4


def step_pot(x):
    if x < 0:
        return (A * exp(1j * k * x)) + (B * exp(-1j * k * x))
    elif x > 0:
        return (C * exp(-kappa * x))


def kinetic(x, h):
    psiold = step_pot(x)

    psip = step_pot(x+h)
    
    psim = step_pot(x-h)
    
    lapl = (psip + psim - (2. * psiold))/h**2

    return -0.5*lapl/psiold