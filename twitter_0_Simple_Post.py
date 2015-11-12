from TwitterAPI import TwitterAPI
from keys import *

api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)


message = "this is my first twitter \n jump line \n again"  

r = api.request('statuses/update', {'status': message})
print(r.status_code)

#error codes 
#https://dev.twitter.com/overview/api/response-codes