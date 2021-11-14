from django.db import models

# Create your models here.
class Data(models.Model):
    query = models.CharField(max_length=500)
    title = models.CharField(max_length=500)
    url = models.CharField(max_length=500)
    des = models.CharField(max_length=500)
    date = models.DateTimeField()
    thumb = models.CharField(max_length=500)