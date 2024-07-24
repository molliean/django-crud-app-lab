# my_app/models.py

from django.db import models
from django.urls import reverse


# Create your models here.

class Architect(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(max_length=1000)
    # place = models.ForeignKey(Place, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('architect-detail', kwargs={'pk': self.id})



class Place(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    style = models.TextField(max_length=100)
    year = models.IntegerField()
    architects = models.ManyToManyField(Architect)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        # Use the 'reverse' function to dynamically find the URL for viewing this place's details
        return reverse('place-detail', kwargs={'place_id': self.id})

DAYS = (
    ('Mon', 'Monday'),
    ('Tue', 'Tuesday'),
    ('Wed', 'Wednesday'),
    ('Thu', 'Thursday'),
    ('Fri', 'Friday'),
    ('Sat', 'Saturday'),
    ('Sun', 'Sunday'),
)

class Hours(models.Model):
    day = models.CharField(max_length=3, choices=DAYS, default=DAYS[0][0])
    open = models.TimeField('Opening Time')
    close = models.TimeField('Closing Time')
    place = models.ForeignKey(Place, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.day}: {self.open} - {self.close}"


