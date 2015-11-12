#Search
from TwitterAPI import TwitterAPI
from time import sleep
from keys import *


api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

SEARCH_TERM = '#london'


r = api.request('search/tweets', {'q': SEARCH_TERM})

for item in r:
    print(item['text'].encode("ascii","ignore") if 'text' in item else item.encode("ascii","ignore"))

print('\nQUOTA: %s' % r.get_rest_quota())
sleep(10)