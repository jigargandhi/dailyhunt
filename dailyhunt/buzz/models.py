from django.db import models
from news.models import Tags
# Create your models here.



class Video(models.Model):
    video_url=models.URLField(verbose_name='video_url',max_length=500)
    tags = models.ManyToManyField(Tags, related_name='videos')
    description = models.CharField(max_length=500)
    icon= models.CharField(max_length=500)
    title=models.CharField(max_length=255)