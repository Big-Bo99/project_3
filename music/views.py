from __future__ import unicode_literals
import youtube_dl

from django.core import serializers
from . import models

from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from .forms import Form
from django.core.mail import send_mail


from .tasks import get_video_code


def index(request):
	if request.method == 'POST':
		form = Form(request.POST)
		if form.is_valid():

			form.save()# Saving form data to model

			youtube_link = form.cleaned_data['youtube_link']
			email = form.cleaned_data['email']

			get_video_code.delay(youtube_link,email)

			#mail.delay(email)


			return render(request, 'music/download.html')

	else:
		form = Form()

	return render(request, 'music/index.html', {'form': form})

def download(request):

	return render(request, 'music/download.html')
