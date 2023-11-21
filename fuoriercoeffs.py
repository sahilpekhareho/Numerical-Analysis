import numpy as np
import matplotlib.pyplot as plt
def f(x):
    return np.exp(np.sin(3*x))
def coeff(n):
    x=np.array([(2*np.pi*(j/n))for j in range (n-1)])
    y=f(x)
    a=[]
    b=[]
    for i in range (n//2):
        pcos=0
        psin=0
        for p in range (n-1):
            pcos+=y[p]*np.cos(i*x[p])
            psin+=y[p]*np.sin(i*x[p])
        a.append((1/(0.5*n))*pcos)
        b.append((1/(0.5*n))*psin)
    return [a,b]
def p(x,n):
    a,b=coeff(n)
    y=0
    for i in range(1,(n//2)-1):
        y+=a[i]*np.cos(i*x)+b[i]*np.sin(i*x)
    y+=0.5*a[0]+0.5*a[(n//2)-1]*np.cos(0.5*n*x)
    return y
print(p(np.pi/2,1000),f(np.pi/2))

plt.figure()
x=np.arange(0,5*np.pi,0.1)
plt.plot(x,p(x,100))

plt.plot(x,f(x))
plt.show()
plt.close()