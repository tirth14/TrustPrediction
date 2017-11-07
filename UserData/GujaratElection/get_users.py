import tweepy

consumer_key = 'XwO0wshECNiLhuGjRoonF7W2l'
consumer_secret = 'Gw9k2k4c4MORSv0oUulWz4SFBZgCxuGTcvDUNZBLyG1lYmUL8M'
access_token = 	'4645330822-CeujMvO5ehaHijViyR0jruddM7jqacAVhDcQsnz'
access_token_secret = 'waLXdJmNfOOZYrO7kKxtrIUSbjoG1CQMlnMI8H37bL4OM' 


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print tweet.text

# file = open('users1.txt', 'w')

# i=1
# for tweet in tweepy.Cursor(api.search, q='#GujaratElection', since='2017-11-01', until='2017-11-05').items(1000):
#     # Do something
#     user = tweet.user.screen_name
#     file.write(user+'\n')
#     print i
#     i+=1

# file.close()
