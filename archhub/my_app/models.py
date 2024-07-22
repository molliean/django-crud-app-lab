from django.db import models
from django.urls import reverse


# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    style = models.TextField(max_length=100)
    year = models.IntegerField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        # Use the 'reverse' function to dynamically find the URL for viewing this cat's details
        return reverse('place-detail', kwargs={'place_id': self.id})