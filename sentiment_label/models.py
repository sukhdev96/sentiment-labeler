from django.db import models
from django.urls import reverse


# Create your models here.

class Post(models.Model):
    source = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)

class Label(models.Model):
    post_ID = models.IntegerField()
    content = models.TextField(blank=True, null=True)
    labeler = models.CharField(max_length=120)
    sentiment = models.CharField(max_length=120)
