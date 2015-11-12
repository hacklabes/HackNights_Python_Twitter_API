## HackNights [Python](https://www.python.org/) the [Twitter API](https://dev.twitter.com/rest/public)

### Starting Installing / Checking your python environment 

Check if you have python installed

####Mac/Linux

1. Go to your terminal emulator 
2. Type `python --version`  and `pip --version`
3. If it doens't work you may need to install it 

####Windows

1. You can use your PowerShell, cmd.exe or install [babun](https://babun.github.io/)
2. type `python -V`


#### Instaling Python 

The easiest is downloading the packages from [Python website](https://www.python.org/downloads/) then [Setuptools](https://pypi.python.org/pypi/setuptools)

####Text Editor

[Sublime](https://www.sublimetext.com/)
[Brackets](http://brackets.io/)

#####Other resources

[Online Python](https://repl.it/languages/python)

[Ipython Notebook](https://ipython.org/notebook.html)

[Online learning](https://www.codecademy.com/learn/python)

### Python and Twitter


####Python Library

Install the library [TwitterAPI](https://github.com/geduldig/TwitterAPI) there are many [others](https://dev.twitter.com/overview/api/twitter-libraries) if you want to have a try.

On your command line tool / terminal type

`pip install TwitterAPI`

####Twitter API Keys

In order to access Twitter through our Python scripts it's necessary to request access and adquire four different keys.

1. You need a Twitter account www.twitter.com
2. Create a new application https://apps.twitter.com/app/new at the **Website** field you can put any website starting with **http** and you can let the field **Callback URL** empty
3. Then go to https://apps.twitter.com/
4. Click on your **App** then click in the tab **Keys and Access Tokens**
5. In the bottom of the page click on  **generate Access Token**, copy the follow keys

```
consumer_key = ""
consumer_secret = ""
access_token_key = ""
access_token_secret = ""
````

if you want to explore the API through the API console https://dev.twitter.com/rest/tools/console


6. Download the zip file from this [repo](https://github.com/hacklabes/HackNights_Python_Twitter_API/archive/master.zip)

7. Edit the file `keys.py` and insert your keys between quotes `""` for each variable

8. Edit the file `twitter_0_Simple_Post.py` and edit the message you want to tweet.

9. To run your script go to your command line tool /terminal 
10. Go to the folder where are all the `.py` files are then type

``python twitter_0_Simple_Post.py``

you may get a number as output, if it is [200](https://dev.twitter.com/overview/api/response-codes) Sucess otherwise have a look at the [error response codes](https://dev.twitter.com/overview/api/response-codes) from twitter

11. Try the other scripts `.py` following these instructions 
