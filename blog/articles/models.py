from django.db import models
import datetime
from django.utils import timezone

from time import time
from django.contrib.auth.models import User
from django.template import RequestContext

def get_upload_file_name(instance, filename):
	return 'uploaded_files/%s_%s' % (str(time()).replace('.','_'),filename)


class Artical(models.Model):
	title = models.CharField(max_length=50)
	alt_title = models.CharField(max_length=50,default="")
	author = models.CharField(max_length=50,default="")
	category = models.CharField(max_length=50,default="")
	star_image = models.FileField(upload_to=get_upload_file_name,default='')
	optional_image = models.FileField(upload_to=get_upload_file_name,null=True, blank=True)
	body = models.TextField()
	pub_date = models.DateTimeField('date published')
	likes = models.IntegerField(default=0)

	def __str__(self):
		return self.title

class Comment(models.Model):
	user_name = models.CharField(max_length=50,default="Guest")
	user_comment = models.TextField(default="None")
	pub_date = models.DateTimeField('date published')
	article = models.ForeignKey(Artical)

	def __str__(self):
		return self.user_comment