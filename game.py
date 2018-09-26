import urllib
import urllib2
from bs4 import BeautifulSoup
url='http://www.allscrabblewords.com/word-description/scramble'
val={'q':'window'}
data=urllib.urlencode(val)
try:
	req=urllib2.Request(url,data)
	response=urllib2.urlopen(req)
	page=response.read()
except Exception as e:
	print str(e)
soup=BeautifulSoup(page, 'html.parser').encode("ascii", "ignore")
with open("wordscrmbl.txt","w+") as fo:
	#for link in soup.find_all('a'):
	fo.write(soup)
	
