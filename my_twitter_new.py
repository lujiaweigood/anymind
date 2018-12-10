# project
# This is a program to get the list of tweets with the given hashtag.
from requests_oauthlib import OAuth1Session
import json
import datetime, time, sys
import key


key_words = input('This is a program to get the list of tweets with the given hashtag \n\
Please enter a hashtag\n(You can start by #,the number of tweets limited to 30)')
print('The hashtag you entered:',key_words)


session = OAuth1Session(key.CK, key.CS, key.AT, key.AS)
url = 'https://api.twitter.com/1.1/search/tweets.json'

try:
    res = session.get(url, params = {'q':key_words, 'count':30})

    if res.status_code != 200:
        print ("Twitter API Error: %d" % res.status_code)
        sys.exit(1)

    print('Accessible times %s' % res.headers['X-Rate-Limit-Remaining'])
    print('Reset time %s' % res.headers['X-Rate-Limit-Reset'])
    sec =int(res.headers['X-Rate-Limit-Reset'])\
               - time.mktime(datetime.datetime.now().timetuple())
    print('Reset time （Convert to remaining seconds） %s' % sec)


    res_text = json.loads(res.text)
    for tweet in res_text['statuses']:
        print('---------------------------------------------------------------------------')
        print('account:',"(fullname:",tweet['user']['name'],'href:',("/"+tweet['user']['screen_name']).strip(),"id:",tweet['user']['id'],')')
        print("date:",tweet['created_at'])
        print("hashtags:",key_words)
        print("favorite count:",tweet['favorite_count'])
        print("retweet_count",tweet['retweet_count'])
        print ("text",tweet['text'])
except:
    print("Can't find the hashtag or can't connect to internet")



# This is a program to get the list of tweets that user has on his feed in json format.
import tweepy
import key

key_words = input('This is a program to get the list of tweets that user has\n\
Please enter a user screen name\n(Please start the user name by @,the number of tweets limited to 30)')
print('The user screen name you entered:',key_words)

consumer_key = key.CK
consumer_secret = key.CS
access_key = key.AT
access_secret = key.AS

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)
try:
    for tweet in tweepy.Cursor(api.user_timeline,screen_name = key_words).items(30):
        print('---------------------------------------------------------------------------')
        print('full_name:',tweet.user.name,"href:",("/"+tweet.user.screen_name).strip(),"id:",tweet.user.id)
        print("date:",tweet.created_at)
        print("user",key_words)
        print("favorite count",tweet.favorite_count)
        print("retweet count",tweet.retweet_count)
        print("text",tweet.text.replace('\n',''))
except:
    print("Can't find the user or can't connect to internet")