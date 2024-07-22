from django.db import models

# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    style = models.TextField(max_length=100)
    year = models.IntegerField()

    def __str__(self):
        return self.name