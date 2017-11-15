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

count_len = [[0 for j in range(n)] for i in range(n)]
index = get_index()

for i in range(n):
	f = open('tweets/user_'+str(i)+'.p','r')
	tweets = cPickle.load(f)
	f.close()
	for tweet in tweets:
		# hashtags = [x['text'].lower() for x in tweet.entities['hashtags']]
		# if not any(['election'.lower() in x for x in hashtags]):
		# 	continue
		# print tweet.id
		if hasattr(tweet,'retweeted_status'):
			parent = tweet.retweeted_status.user.screen_name
			if parent in index:
				j = index[parent]
				count_len[j][i] += len(tweet.text)
		elif hasattr(tweet,'quoted_status'):
			parent = tweet.quoted_status['user']['screen_name']
			if parent in index:
				j = index[parent]
				count_len[j][i] += len(tweet.text)
	print i

f = open('conv_lens.p','w')
cPickle.dump(count_len,f)
f.close()