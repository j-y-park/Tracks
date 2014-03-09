from django.db import models
from django.utils import timezone
import os

# Create your models here.
class Track(models.Model):
    filename = models.CharField(max_length=50)
    filepath = models.CharField(max_length=200)

    def __unicode__(self):
        return self.filename



def handle_upload_file(f, track, path="..\\Tracks\\TracksApp\\user_mp3_files"):
    ##print(path)
    temp_dest = os.path.join(path, timezone.datetime.now().strftime('%m-%d-%Y_%H-%M-%S'))
    print(temp_dest)
    with open(temp_dest,'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    track.filepath = temp_dest
    track.save()
    return temp_dest