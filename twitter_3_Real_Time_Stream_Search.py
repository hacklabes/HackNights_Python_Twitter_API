#Stream 
from TwitterAPI import TwitterAPI
from keys import *


api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

TRACK_TERM = 'emoji'

r = api.request('statuses/filter', {'track': TRACK_TERM})
for item in r:
    print(item['text'])
