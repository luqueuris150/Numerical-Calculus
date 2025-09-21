import numpy as np

# Oi pró! Não vou implementar um tratamento de erros mais detalhado pq
# To um pouquinho sem tempo. Só a função mesmo e um input básico.
# Abração!
# Lucas Pereira de Souza

def Vandermonde(x):
    grau = len(x)
    A = []
    for i in np.arange(0,grau,1):
        linha = []
        for j in np.arange(0,grau,1):
            linha.append(x[i]**j)
        A.append(linha)
    A = np.flip(A,1)
    return A

loop = int(input('Quantos pontos você deseja adicionar? '))
x = []
for i in range(loop):
    num = float(input('Digite o número %i: '%(i+1)))
    x.append(num)

A = Vandermonde(x)
A = np.array(A)

print('Sua matriz de Vandermonde será: ')
print('A = ')
print(A)
