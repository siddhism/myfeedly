from django.db import models
from django.utils.encoding import smart_unicode

# Create your models here.
class RssUrl(models.Model):
	url = models.CharField(max_length=100, unique=True)
	def __unicode__(self):
		return smart_unicode(self.url)

class Dummy(models.Model):
	name = models.CharField(max_length = 100)
	def __unicode__(self):
		return smart_unicode(self.name)