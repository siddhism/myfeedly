from django.contrib import admin

# Register your models here.
from .models import RssUrl

class RssUrlAdmin(admin.ModelAdmin):
	class Meta:
		model = RssUrl

admin.site.register(RssUrl, RssUrlAdmin)