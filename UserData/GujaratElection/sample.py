import tweepy
import time
consumer_key = 'XwO0wshECNiLhuGjRoonF7W2l'
consumer_secret = 'Gw9k2k4c4MORSv0oUulWz4SFBZgCxuGTcvDUNZBLyG1lYmUL8M'
access_token = 	'4645330822-CeujMvO5ehaHijViyR0jruddM7jqacAVhDcQsnz'
access_token_secret = 'waLXdJmNfOOZYrO7kKxtrIUSbjoG1CQMlnMI8H37bL4OM' 


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# print 'hi'
# time.sleep(10)
# print 'hello'

# g = open('users.txt','r')
# users = [i.strip() for i in g.readlines()[:200]]

import cPickle              # import module first

f = open('tweets/user_5.p', 'r')   # Pickle file is newly created where foo1.py is
tweets = cPickle.load(f)          # dump data to f

print len(tweets)
print [tweet.text for tweet in tweets]
