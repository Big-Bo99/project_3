from django.db import models
from django.forms import ModelForm

class Download(models.Model):
	email = models.CharField(max_length=500)	
	youtube_link = models.CharField(max_length=500)
	pub_date = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.youtube_link
	def was_published(self):
		return self.pub_date
