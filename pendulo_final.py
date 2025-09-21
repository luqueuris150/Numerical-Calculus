import numpy as np

def integral(f,ddf,xi,xf,h):
    x = np.arange(xi,xf,h)
    s = 0
    for i in np.arange(0,len(x)-1,1):
        s = s + (h/2)*(f(x[i])+f(x[i+1])) - ((h**3)/12)*ddf((x[i]+x[i+1])/2)
    return s

l = 1.0
g = 9.8
w = np.sqrt(l/(2*g))
theta0 = np.pi/2

f = lambda theta: (1/np.sqrt(np.cos(theta)-np.cos(theta0)))

ddf = lambda theta: 0.5*(f(theta)**3)*(np.cos(theta) + (3*np.sin(theta)/2)*f(theta))

T = 4*w*integral(f,ddf,0.,theta0,0.00001)
print(T)
e = 2.3690497221753	
print(T-e)
print(np.abs(T-e)/e)
