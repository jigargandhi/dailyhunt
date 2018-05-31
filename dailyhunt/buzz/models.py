from django.db import models
from news.models import Tags
# Create your models here.



class Video(models.Model):
    video_url=models.URLField(verbose_name='video_url',max_length=500)
    tags = models.ManyToManyField(Tags, related_name='videos')
    description = models.CharField(max_length=500)
    icon= models.CharField(max_length=500)
    thumbnail_url = models.URLField(name='thumbnail_url',max_length=4096,default='')
    title=models.CharField(max_length=255)

    def get_url(self):
        return self.video_url