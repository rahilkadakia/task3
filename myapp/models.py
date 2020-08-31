from django.db import models
from django.contrib.auth.models import User
import datetime

class Events(models.Model):
    name = models.CharField(max_length=100, default='no_name')
    date = models.DateField(default=datetime.date.today)
    location = models.CharField(max_length=200, default='no_name')
    notes = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField('img', upload_to='media', blank=True, null=True)