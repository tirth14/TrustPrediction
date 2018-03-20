import tweepy
import cPickle
import json
import random
import numpy as np

#number of users
N=5268

def get_index():
    file = open('users.txt','r')
    users = [i.strip() for i in file.readlines()][:N]
    file.close()
    index = dict()
    i = 0
    for user in users:
        index[user] = i
        i += 1
    return index

count_tweet = [0 for i in range(N)]
count_retweet = [[] for j in range(N)]
index = get_index()

for i in range(N):
    f = open('tweets/user_'+str(i)+'.p','r')
    tweets = cPickle.load(f)
    f.close()
    count_tweet[i] = len(tweets)
    count_retweet[i] = [0 for j in range(count_tweet[i])]
    for (j,tweet) in enumerate(tweets):
        count_retweet[i][j] += tweet.retweet_count
    print i,count_tweet[i],"	|",

# count_tweet[:10]

sd = np.zeros(N)
avg = np.zeros(N)
consistency = np.zeros(N)
for i in range(N):
    sd[i] = np.std( np.asarray(count_retweet[i] )) 
    avg[i] = np.mean( np.asarray(count_retweet[i] )) 

# print np.mean(count_retweet, axis = 0)

print sd.shape   , avg.shape 
print sd[0], avg[0], avg[0]/sd[0]

consistency = avg/sd


f = open('consistency.p', 'w')
cPickle.dump(consistency, f)
f.close()