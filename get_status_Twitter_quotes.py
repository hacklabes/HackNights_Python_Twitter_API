from TwitterAPI import TwitterAPI
from keys import *

api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)


r = api.request('application/rate_limit_status')

j = r.response.json()

print(j['resources']['statuses'])
print("\n")
print(j['resources']['search'])
print("\n")
print(j['resources']['geo'])
