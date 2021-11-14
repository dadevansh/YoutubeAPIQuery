from django.db import models

# Create your models here.
class Data(models.Model):
    _id = models.CharField(max_length=500)
    query = models.CharField(max_length=500)
    title = models.CharField(max_length=500)
    url = models.CharField(max_length=500)
    des = models.CharField(max_length=500)
    date = models.DateTimeField()
    thumb = models.CharField(max_length=500)
    
    def __str__(self):
        return "{" + \
            "'_id':" + self._id + ", " + \
            "'query':" + self.query + ", " + \
            "'title':"  + self.title + ", "+ \
            "'url':" + self.url + ", "+ \
            "'des':"  +self.des + ", " + \
            "'date':"  +str(self.date) + ", " + \
            "'thumb':"  +self.thumb + ", " + \
        "}"