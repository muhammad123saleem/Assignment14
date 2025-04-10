from django.db import models

# Create your models here.

class Hotel(models.Model):
    name = models.CharField(max_length=75)
    address = models.CharField(max_length=75)
    number_of_rooms = models.IntegerField()
    occupied_rooms = models.IntegerField()

    def __str__(self):
        return self.name


