from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Statement(models.Model):
    sentence = models.CharField(max_length=200)
    blank = True
    number = models.IntegerField()
    def __self__(self):
        return self.sentence
