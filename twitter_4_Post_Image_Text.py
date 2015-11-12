#Stream 
from TwitterAPI import TwitterAPI
from keys import *


api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

	


TWEET_TEXT = 'some tweet text'
IMAGE_PATH = 'cat.gif'


file = open(IMAGE_PATH, 'rb')
data = file.read()
r = api.request('statuses/update_with_media',
                {'status': TWEET_TEXT},
                {'media[]': data})

print('SUCCESS' if r.status_code == 200 else 'FAILURE')