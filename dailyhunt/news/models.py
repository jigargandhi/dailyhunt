from django.db import models

# Create your models here.

class Language(models.Model):
    name=models.CharField(max_length=50,blank=False)
    code= models.CharField(max_length=2,blank=False)

    def __str__(self):
        return "[{} - {}]".format(self.name, self.code)


class Tags(models.Model):
    name=models.CharField(max_length=50,blank=False, unique=True)
    language=models.ForeignKey(Language, related_name='tags', on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class News(models.Model):
    title=models.CharField(max_length=255, unique=False,blank=False)
    subtitle=models.CharField(max_length=100, null=True,blank=True)
    is_archived= models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    publish_date=models.DateTimeField()
    language=models.ForeignKey(Language,related_name='news', on_delete= models.CASCADE)
    tags= models.ManyToManyField(Tags)
    content=models.TextField(verbose_name='Content',default='')
