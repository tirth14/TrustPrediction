import random

def influence(P,j):
	return sum([u[j][i]*I[i] for i in range(n)])

def passivity(I,j):
	return sum([v[i][j]*I[i] for i in range(n)])

def edge(i,j):
	return True

# number of nodes
n = 10

w1 = [[random.random() for j in range(n)] for i in range(n)]
w2 = [[1-w1[i][j] for j in range(n)] for i in range(n)]

u = [[0 for j in range(n)] for i in range(n)]
v = [[0 for j in range(n)] for i in range(n)]

sum_col_w1 = [sum([w1[j][i] for j in range(n)]) for i in range(n)]
sum_row_w2 = [sum(w2[i]) for i in range(n)]


for i in range(n):
	for j in range(n):
		if edge(i,j):
			u[i][j] = w1[i][j]/sum_col_w1[j]

for i in range(n):
	for j in range(n):
		if edge(j,i):
			v[j][i] = w2[j][i]/sum_row_w2[j]

# print w1[0],w2[0]

I = [1 for i in range(n)]
P = [1 for i in range(n)]

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
	print max(I), sum(I)

print I
