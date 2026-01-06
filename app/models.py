from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100)
    urltag = models.CharField(max_length=1000)
    tag = models.CharField(max_length=1000, default='app')
    info = models.TextField(default="lorem")