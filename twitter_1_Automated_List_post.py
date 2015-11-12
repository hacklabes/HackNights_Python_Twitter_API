from TwitterAPI import TwitterAPI
from time import sleep
from keys import *

api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

messageTemplate= "this is "
words = ["sad", "happy", "boring", "gorgeous", "brillant"]

#the length of our words list
numMsgs = len(words)


for word in words:
	#range give us a list of indexs [0,1,2,3 .. numMsgs] 
	message = messageTemplate + " " + word
	print message	
	#request to update the status
	r = api.request('statuses/update', {'status': message})
	
	#post and return the error
	#error codes 
	#https://dev.twitter.com/overview/api/response-codes
	print(r.status_code)
	sleep(1) #sleep one second posting each message

#THE END