from django.db import models

# Create your models here.
class Shortener(models.Model):
    link = models.URLField(max_length=250)
    shlink = models.CharField(max_length=5)
    length = shlink.max_length
