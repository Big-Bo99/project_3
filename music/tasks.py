import string
import youtube_dl
from youtube_dl import YoutubeDL
from django.core.mail import send_mail
from django.template.defaultfilters import slugify

from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

from celery import shared_task, task
from celery import Celery

@task
def get_video_code(youtube_link,email):

#Geting the name of a song

    y = YoutubeDL({
        'format': 'bestaudio',
    })

    r = y.extract_info(youtube_link, download=False)
    file_name = r['title'].replace(" ", "_")

#Downloading song

    ydl_opts = {

        'outtmpl': 'media/songs/' + file_name + '.%(ext)s',
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_link])

#Sending Email

    send_mail(
        'Your song',
        'Here is your download: http://127.0.0.1:8000/media/songs/' + file_name + '.mp3',
        'from@example.com',
        [email],
        fail_silently=False,
    )
