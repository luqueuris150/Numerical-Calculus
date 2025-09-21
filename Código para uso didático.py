import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme()
import numpy as np

def newton_raphson(x0, f, df, e, xlvec):

	xl = x0 - f(x0)/df(x0)
	xlvec.append(x0)
	xlvec.append(xl)
	i=0
	while np.abs(f(xl)) > e:
		#if i%10:
		#	print(f'{xl:+.6f}, {f(xl):+.6f}')
		xl = xl - f(xl)/df(xl)
		xlvec.append(xl)
		i+=1

	return xl

h = 6.64*1e-34
c = 299792458
k = 1.3806503*1e-23

f  = lambda x: (x-5)*np.exp(x)+5
df = lambda x: (x-4)*np.exp(x)

fl = lambda x,T: h*c/(x*k*T)

T = np.linspace(500, 2000, 10000)

Tbt = 500
Tup = 2000

xlvec = []
xm = newton_raphson(4.5, f, df, 1e-3, xlvec)

#print(xm, "---->", f(xm))

#fig = plt.figure()
#ax = fig.add_subplot()

#ax.plot(x, f(x), c='b')

#ax.scatter(xm, f(xm))
#ax.set_title("Derivada da Densidade de Energia em função de x $\\left(\\frac{hc}{k \\lambda T}\\right)$")
#ax.set_xlabel("x")
#ax.set_ylabel("f(x)")
#ax.set_ylim([-55,10])
#fig.tight_layout()

xm = max(xlvec)

for i,xl in enumerate(xlvec):
	print(f'xl {xl} df(xl) {df(xl)} f(xl) {f(xl)}')
	
	x = np.linspace(0, 6, 40)

	fig = plt.figure(i)
	ax = fig.add_subplot()

	ax.plot(x, f(x), c='b')
	ax.scatter(xl, f(xl))
	ax.plot(x, df(xl)*(x-xl) + f(xl), c='k')

	ax.set_title("Derivada da Densidade de Energia em função de x $\\left(\\frac{hc}{k \\lambda T}\\right)$\nPasso "+str(i)+" xl="+str(xl))
	ax.set_xlabel("x")
	ax.set_ylabel("f(x)")
	ax.set_ylim([-55,95])
	ax.set_xlim([0,xm+1])
	fig.tight_layout()
	fig.savefig(f'images/{i}.svg')
	
	xi = xl-f(xl)/df(xl)
	ax.plot([xi, xi], [0, f(xi)], '--m')

	fig.savefig(f'images/{i}_0.svg')
	plt.close(fig)

#fig2 = plt.figure()
#bx = fig2.add_subplot()
#bx.plot(T, fl(xm,T), c='r')
#bx.set_title("Comprimento de onda em função da Temperatura")
#bx.set_xlabel("T (K)")
#bx.set_ylabel("$\\lambda$ (m)")
#fig2.tight_layout()

#plt.show()
