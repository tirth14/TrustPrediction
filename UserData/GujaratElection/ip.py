import random
import cPickle
# number of nodes
# n = 10
# w1 = [[random.random() for j in range(n)] for i in range(n)]

def get_index():
	file = open('users.txt','r')
	users = [i.strip() for i in file.readlines()][:n]
	file.close()
	index = dict()
	i = 0
	for user in users:
		index[user] = i
		i += 1
	return index


file = open('users.txt','r')
users = [i.strip() for i in file.readlines()]
file.close()

f = open('weights.p', 'r')
w1 = cPickle.load(f)
f.close()

n = len(w1)
w2 = [[1.0-w1[i][j] for j in range(n)] for i in range(n)]

u = [[0.0 for j in range(n)] for i in range(n)]
v = [[0.0 for j in range(n)] for i in range(n)]

sum_col_w1 = [sum([w1[j][i] for j in range(n)]) for i in range(n)]
sum_row_w2 = [sum(w2[i]) for i in range(n)]


# print w1[:10] 
# print w2[:10]
# print u[:10]
# print v[:10]
# print sum_col_w1[:10]
# print sum_row_w2[:10]

def influence(P,j):
	return sum([u[j][i]*P[i] for i in range(n)])

def passivity(I,j):
	return sum([v[i][j]*I[i] for i in range(n)])

def edge(i,j):
	return w1[i][j]!=0

for i in range(n):
	for j in range(n):
		if edge(i,j):
			u[i][j] = w1[i][j]/sum_col_w1[j]

for i in range(n):
	for j in range(n):
		if edge(j,i):
			v[j][i] = w2[j][i]/sum_row_w2[j]

# print w1[0],w2[0]

I = [1.0 for i in range(n)]
P = [1.0 for i in range(n)]

for i in range(20):
	I_sum = 0
	P_sum = 0
	for j in range(n):
		P[j] = passivity(I,j)
		P_sum += P[j] 
	for j in range(n):
		I[j] = influence(P,j)
		I_sum += I[j]
	print I[0], I_sum
	for j in range(n):
		if I_sum!=0:
			I[j] /= I_sum 
		if P_sum!=0:
			P[j] /= P_sum
	# print max(I), sum(I)

# print I

index = get_index()
inf = [(I[i],users[i]) for i in range(n)]
inf.sort(reverse=True)

for i in range(100):
	id_ = index[inf[i][1]]
	# print inf[i], id_, sum(w1[id_]) 
	print inf[i],
	print "	"+str(id_)+"	"+ str(200*sum(w1[id_]) ) 


f = open('influence.p', 'w')
cPickle.dump(I, f)
f.close()