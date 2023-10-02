from django.db import models


class ThingUser(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    quantity = models.IntegerField()


# Create your models here.