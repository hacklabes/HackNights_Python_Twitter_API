import urllib

def thisIsaFunction(a,b):
	return a + b


for count in range(100):
	print count
	print "hello world"
	print thisIsaFunction(count,count)


website = "www.google.com"

url = urllib.urlopen("http://" + website)
text = url.readlines()

print text

fileName = website + ".html"
f = open(fileName, "w")
f.writelines(text)
f.close()


