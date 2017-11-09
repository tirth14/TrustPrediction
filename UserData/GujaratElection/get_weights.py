import tweepy
import cPickle
import json

# number of users
n = 5268

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

count_retweet = [[0 for j in range(n)] for i in range(n)]
count_tweet = [0 for i in range(n)]
index = get_index()

for i in range(n):
	f = open('tweets/user_'+str(i)+'.p','r')
	tweets = cPickle.load(f)
	f.close()
	for tweet in tweets:
		count_tweet[i] += 1 # can make it constrained in a time period
		if hasattr(tweet,'retweeted_status'):
			parent = tweet.retweeted_status.user.screen_name
			if parent in index:
				j = index[parent]
				count_retweet[i][j] += 1
		elif hasattr(tweet,'quoted_status'):
			parent = tweet.quoted_status['user']['screen_name']
			if parent in index:
				j = index[parent]
				count_retweet[i][j] += 1
	print i

w = [[0.0 for j in range(n)] for i in range(n)]
for i in range(n):
	if count_tweet[i]!=0:
		w[i] = [float(count_retweet[i][j])/count_tweet[i] for j in range(n)]
		# print sum(count_retweet[i]), sum(w[i])

f = open('weights.p','w')
cPickle.dump(w,f)
f.close()
