from django.db import models
from django.urls import reverse


# Create your models here.

class Course(models.Model):
    title       = models.CharField(max_length=120) # max_length = required

def get_absolute_url(self):
        return reverse("courses:course-detail", kwargs={"id": self.id}) #f"/products/{self.id}/"
