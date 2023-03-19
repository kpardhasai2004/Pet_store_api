from django.db import models

# Create your models here.
class pets(models.Model):
    idno = models.PositiveBigIntegerField()
    name = models.CharField(max_length=100)
    parent = models.CharField(max_length=225)
    type = models.CharField(max_length=225)
    age = models.IntegerField()
    gender = models.CharField(max_length=225)