import datetime

from django.db import models

# Create your models here.
class Activity(models.Model):
    username = models.CharField(max_length=256, default="wcz")
    isTemp = models.BooleanField(default=True)
    title = models.CharField(max_length=256, default="")
    startDate = models.DateField(default=datetime.date.today)
    endDate = models.DateField(default=datetime.date.today)
    coordinate = models.CharField(max_length=256, default="")
    participant = models.CharField(max_length=256, default="")
    description = models.CharField(max_length=16384, default="")

    detail_title = models.CharField(max_length=256, default="")
    detail_text = models.CharField(max_length=16384, default="")

    photo_path = models.CharField(max_length=16384, default="")
    video_path = models.CharField(max_length=16384, default="")

