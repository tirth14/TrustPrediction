# f1 = open('users1.txt', 'r')
# f2 = open('users2.txt', 'r')
# f3 = open('users3.txt', 'r')
# f4 = open('users4.txt', 'r')
# f5 = open('users5.txt', 'r')

# users1 = [i.strip() for i in f1.readlines()]
# users2 = [i.strip() for i in f2.readlines()]
# users3 = [i.strip() for i in f3.readlines()]
# users4 = [i.strip() for i in f4.readlines()]
# users5 = [i.strip() for i in f5.readlines()]

# users_set = set(users1+users2+users3+users4+users5)

# file = open('users.txt', 'w')

# for user in users_set:
# 	file.write(user+'\n')

# print len(users_set)

# import os

# missing = [1356, 2010, 3718, 3855, 3858, 3870, 4822, 5141]

# c=0
# for i in range(1,5277):
# 	if i not in missing:
# 		os.rename('tweets/user_'+str(i)+'.p', 'tweets/user_'+str(c)+'.p')
# 		c+=1
# 	else:
# 		print i
