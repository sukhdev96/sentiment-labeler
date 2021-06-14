from django.db import models
from django.urls import reverse


# Create your models here.

class Post(models.Model):
    source = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    no_of_labels = models.IntegerField(default=0)

class Label(models.Model):
    post_ID = models.IntegerField()
    labeler = models.CharField(max_length=120)
    sentiment = models.CharField(max_length=120)
    timestamp = models.DateTimeField(auto_now_add=True)
