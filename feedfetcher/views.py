from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect
from BeautifulSoup import BeautifulSoup
from django.core import serializers

from .forms import *
from .feeds import *
from feedfetcher.tasks import parseAllFeeds

# Create your views here.
def home(request):
	form = RssUrlForm(request.POST or None)
	#added dummy comment
	all_subscriptions = RssUrl.objects.all()
	if form.is_valid():
		save_it = form.save(commit= False)
		save_it.save()
		form = RssUrlForm()
		all_subscriptions = RssUrl.objects.all()
		# result = parseAllFeeds.delay(all_subscriptions)
		
		return render_to_response('index.html',locals(),
			context_instance = RequestContext(request))
	
	result = parseAllFeeds.delay('just a test')

	# # check for result from celery	
	# getting error celery backend setting

	if result.ready():
		print "Task has run"
		if result.successful():
			print "Result was: %s" % result.result
		else:
			if isinstance(result.result, Exception):
				print "Task failed due to raising an exception"
				raise result.result
			else:
				print "Task failed without raising exception"
	else:
		print "Task has not yet run"
	
	return render_to_response('index.html',locals(),
			context_instance = RequestContext(request))

def result(request, url_id):
	# pass
	obj = RssUrl.objects.get(pk = url_id)
	url = obj.url
	# print url
	data = parseFeed(url)
	# print data
	return render_to_response('result.html',locals(),
		context_instance = RequestContext(request))
