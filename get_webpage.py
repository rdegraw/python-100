import urllib2, sys, re
from bs4 import BeautifulSoup
import windows_crap

if sys.platform == "win32":
	windows_crap.setup_win()
	
#url = raw_input( 'Enter a URL: ' )
url = "http://www.fftoday.com"

soup = BeautifulSoup(urllib2.urlopen(url).read())

print soup.title
for link in soup.find_all(href=re.compile("cheatsheets")):
	player_ranks = link.get('href')

if player_ranks:
	print player_ranks

	soup = BeautifulSoup(urllib2.urlopen( player_ranks ))
	for link in soup.find_all("a"):
		print ( link.get('href') )
	

