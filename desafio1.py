

# input list
#x = [93.3, 98.9, 104.4]
x = [93.3, 98.9, 104.4, 112, 2.31, 213., 1, 2, 3]
n = len(x)

A = []

for i in range(n):
	A.append([])
	for j in range(n):
		A[i].append(x[j]**j)



print(' '*21+(' '*19).join(['A'+str(i+1) for i in range(n)])+'\n')

for i in range(n):
	print('A'+str(i+1)+' ', end='')
	for j in range(n-1):
		print(f'{A[i][j]: >20.2f},', end='')
	print(f'{A[i][j]: >20.2f}')
