import matplotlib.pyplot as plt
import numpy as np

def integral(f,ddf,x,h):
    s = 0
    for i in np.arange(0,len(x)-1,1):
        s = s + (h/2)*(f(x[i])+f(x[i+1])) - ((h**3)/12)*ddf((x[i]+x[i+1])/2)
    return s

l = 1.0
g = 9.8
w = np.sqrt(l/(2*g))
theta0 = np.pi/2
#h = 1e-5
e = 2.3690497221753	
expoentes = np.linspace(1, -5, 75)

f = lambda theta: (1/np.sqrt(np.cos(theta)-np.cos(theta0)))

ddf = lambda theta: 0.5*(f(theta)**3)*(np.cos(theta) + (3*np.sin(theta)/2)*f(theta))

erros = []

for h in 10.0**expoentes:
	print(h)
	x = np.arange(0.,theta0,h)
	T = 4*w*integral(f,ddf,x,h)
	err = np.abs(T-e)/e
	erros.append(err)

fig, ax = plt.subplots(1,1,figsize=(16,9))

#plt.hline([0, x[-1]], e, c='b', label='Valor teórico')

ax.plot(expoentes, erros, c='#ef405d', label='erro relativo', alpha=.5)

ax.invert_xaxis()

ax.set_ylabel('Erro relativo (%)')
ax.set_xlabel('Ordem de grandeza do passo (10^x)')

fig.tight_layout()

fig.savefig('erro_relativo.svg')
