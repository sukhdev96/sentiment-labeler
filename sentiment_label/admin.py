from django.contrib import admin

# Register your models here.

from .models import Sentiment

admin.site.register(Sentiment)