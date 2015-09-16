from __future__ import absolute_import

from celery import shared_task
from django.core import serializers

import urllib2
from BeautifulSoup import BeautifulSoup
import feedparser

from .models import *

@shared_task
def parseAllFeeds(arg):
	all_data = {}
	all_objects = RssUrl.objects.all()
	for item in all_objects:
		url = item.url
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
		all_data['url'] = feed["items"]
	
	return all_data
	# return 'The test task executed with argument "%s" ' % param