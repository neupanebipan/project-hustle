from django.db import models
from embed_video.fields import EmbedVideoField
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
#creating database for posting blogs.

class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, default=" Our fitness blogs!!")
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    body = models.TextField()
    def __str__(self):
        return self.title + ' | ' + str(self.author)
        
    def get_absolute_url(self):
        return reverse( 'article-detail' , args = [str(self.id)])

  



