from django.db import models
from django.urls import reverse


# Create your models here.

class Sentiment(models.Model):
    source = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    author_1 = models.CharField(max_length=120 , blank=True, null=True)
    author_2 = models.CharField(max_length=120, blank=True, null=True)
    author_3 = models.CharField(max_length=120, blank=True, null=True)
    sentiment_1 = models.CharField(max_length=120, blank=True, null=True)
    sentiment_2 = models.CharField(max_length=120, blank=True, null=True)
    sentiment_3 = models.CharField(max_length=120, blank=True, null=True)