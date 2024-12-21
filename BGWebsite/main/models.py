from django.db import models

# Create your models here.
class Activity(models.Model):
    username = models.CharField(max_length=256, unique=True)
    isTemp = models.BooleanField()
    title = models.CharField(max_length=256)
    startDate = models.DateField()
    endDate = models.DateField()
    coordinate = models.CharField(max_length=256)
    participant = models.CharField(max_length=256)
    description = models.CharField(max_length=16384)

class ActivityDetail(models.Model):
    activity = models.OneToOneField(Activity, on_delete=models.CASCADE, related_name='activity_detail')
    title = models.CharField(max_length=256)
    text = models.TextField()

class Photo(models.Model):
    activity_detail = models.ForeignKey(ActivityDetail, on_delete=models.CASCADE, related_name='photos')
    photo = models.FileField(upload_to='upload/%Y/%m/%d/%H/%M/%S/', null=True, blank=True)

class Video(models.Model):
    activity_detail = models.ForeignKey(ActivityDetail, on_delete=models.CASCADE, related_name='videos')
    video = models.FileField(upload_to='upload/%Y/%m/%d/%H/%M/%S/', null=True, blank=True)