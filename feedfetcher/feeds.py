import urllib2
from BeautifulSoup import BeautifulSoup
import feedparser

def parseFeed(url):
	page = urllib2.urlopen(url)
	soup = BeautifulSoup(page)
	link = soup.find('link', type='application/rss+xml')
	if link:
		finalurl = link['href']
		if finalurl.startswith("/"):
			finalurl = url + link['href']
			feed = feedparser.parse( finalurl )
			# print finalurl
		elif finalurl:
			feed = feedparser.parse( finalurl )
	else:
		feed = feedparser.parse( url )
	return feed["items"]