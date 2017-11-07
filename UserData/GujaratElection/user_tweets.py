import tweepy
import cPickle
import time

# Tirth
consumer_key = 'XwO0wshECNiLhuGjRoonF7W2l'
consumer_secret = 'Gw9k2k4c4MORSv0oUulWz4SFBZgCxuGTcvDUNZBLyG1lYmUL8M'
access_token = 	'4645330822-CeujMvO5ehaHijViyR0jruddM7jqacAVhDcQsnz'
access_token_secret = 'waLXdJmNfOOZYrO7kKxtrIUSbjoG1CQMlnMI8H37bL4OM' 

# Ambar
# consumer_key = 'jnL5aPjQIsliJsaBBGmaoi7JG'
# consumer_secret = 'E5yShz3JzGIlKsq5F7i2ormVJzhHA9iQVkSU1Mr4BBHDcDbC3b'
# access_token = 	'927959442582155269-O2BVnxBZWVOdgfndzvjWmW9Hb60ccZJ'
# access_token_secret = 'd6xV3mB3fI2SoxhtPd2jclIjrFBcCGBvk1EPZk3m9MzUq' 

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

g = open('users.txt','r')
users = [i.strip() for i in g.readlines()]

print len(users)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print tweet.text

# print [tweet.text for tweet in api.user_timeline(screen_name='rd99rocks', count=200)]

def get_tweets(user):
	try:
		tweets = api.user_timeline(screen_name=user, count=200)
		return tweets
	except Exception:
		time.sleep(60)
		print 'trying again in a minute'
		return get_tweets(user)

for i in range(2010,3200):
	tweets = []
	public_tweets = get_tweets(users[i])
	for tweet in public_tweets:
	    tweets.append(tweet)
	f = open('tweets/user_'+str(i+1)+'.p', 'w')
	cPickle.dump(tweets, f)
	f.close()
	print i, len(tweets)

print i, 'finished'