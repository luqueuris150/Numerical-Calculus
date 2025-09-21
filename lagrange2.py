import numpy as np

# Mais uma vez, fiz algo simples

def Lk(x,k,xv,grau): # Função do Lk no polinômio
    numerador = 1
    denominador = 1
    graumax = len(xv)
    if grau == 0:
        grau = graumax
    contador = 1
    for i in np.arange(0,graumax,1):
        if i == k:
            continue
        else:
            numerador = numerador*(x - xv[i])
            denominador = denominador*(xv[k] - xv[i])
            contador = contador + 1
            if contador == grau:
                break
    result = numerador/denominador
    return result

def Pn(x,y,xv,grau): # Função do Polinômio
    graumax = len(xv)
    if grau == 0:
        grau = graumax
    p = 0
    for j in np.arange(0,graumax,1):
        p = p + y[j]*Lk(x,j,xv,grau)
    return p

xv = [-1.0, 0.0, 2.0] # pontos xi pra testar
y = [4.0, 1.0, -1.0] # pontos yi = f(xi) pra testar
# Grau do polinômio, para teste. Se grau = 0, vamos usar o grau máximo
grau = int(input('Qual grau do polinômio você deseja? '))
while 1:
    if grau > len(xv):
        print('O polinômio não pode ter grau maior que a quantidade de valores fornecida.')
        grau = int(input('Qual grau do polinômio você deseja? '))
    else:
        x = 1.0 # Novo ponto pra testar
        teste = Pn(x,y,xv,grau)
        break

print('O resultado do polinômio para o ponto %.2f será: %.2f ' %(x,teste))
