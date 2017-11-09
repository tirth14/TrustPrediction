import random

# number of nodes
n = 100

u = [[random.random() for j in range(n)] for i in range(n)]
v = [[random.random() for j in range(n)] for i in range(n)]

# print u[0],v[0]

I = [1 for i in range(n)]
P = [1 for i in range(n)]

def influence(P,j):
	return sum([u[j][i]*I[i] for i in range(n)])

def passivity(I,j):
	return sum([v[i][j]*I[i] for i in range(n)])

for i in range(5):
	I_sum = 0
	P_sum = 0
	for j in range(n):
		P[j] = passivity(I,j)
		P_sum += P[j] 
	for j in range(n):
		I[j] = influence(P,j)
		I_sum += I[j]
	# print I[0], I_sum
	for j in range(n):
		I[j] /= I_sum
		P[j] /= P_sum
	# print max(I), sum(I)

# print I, P