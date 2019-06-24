from django.db import models
import datetime as dt
from django.contrib.auth.models import User

class Project(models.Model):
    image = models.ImageField(upload_to = 'images/', null =True, blank = True, default = '../static/images/noimage.svg')
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length = 500)
    technologies = models.CharField(max_length = 100)
    github = models.CharField(max_length = 100)
    live = models.CharField(max_length = 100)
