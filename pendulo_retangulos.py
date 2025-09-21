import numpy as np
import matplotlib.pyplot as plt

def integral(f,ddf,x,h):
	s = 0
	k=0
	for i,j in zip(x[:-1], x[1:]):
		plt.plot([i, i], [0, f(i)], '--', c='#ef405d', alpha=.5)
		plt.plot([i, j], [f(i), f(j)], '--', c='#ef405d', alpha=.5)
		plt.plot([j, j], [f(j), 0], '--', c='#ef405d', alpha=.5)

		xx = np.linspace(i, j, 10)
		yy = np.linspace(f(i), f(j), 10)

		plt.fill_between(xx, f(xx), yy, color='pink')

		area = (h/2)*(f(i)+f(j))
		erro = ((h**3)/12)*ddf((i+j)/2)

		a = i+(j-i)/2.
		b = f((j-i)/2+i)/2.
		c = f(i)+(f(j)-f(i))/2.
		if k%5==0:
			plt.annotate(f'Area\n{area:3.2}', (a, b), xytext=(a-.01, b-.3), arrowprops=dict(arrowstyle='->', color='k', lw=1, ls='-') )
			plt.annotate(f'Erro\n{erro:3.2}', (a, c), xytext=(a-.05, c+.15), arrowprops=dict(arrowstyle='->', color='k', lw=1, ls='-') )

		k+=1
		s = s + area - erro
	return s

l = 1.0
g = 9.8
w = np.sqrt(l/(2*g))
theta0 = np.pi/2

for N in [3, 10, 50, 100]:
	h = theta0/N
	x = np.linspace(0.,theta0-1e-2,N)
	
	f = lambda theta: (1/np.sqrt(np.cos(theta)-np.cos(theta0)))
	
	ddf = lambda theta: 0.5*(f(theta)**3)*(np.cos(theta) + (3*np.sin(theta)/2)*f(theta))
	
	fig, ax = plt.subplots(1,1,figsize=(16,9))
	
	xx = np.linspace(0, x[-1], 100)
	ax.plot(xx, f(xx), label='f')
	
	T = 4*w*integral(f,ddf,x,h)

	ax.set_ylabel('$f(\\theta)$')
	ax.set_xlabel('$\\theta$')
	
	fig.tight_layout()
	
	fig.savefig(f'areas_{N}.svg')


