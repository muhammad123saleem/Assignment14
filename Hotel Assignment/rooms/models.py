from django.db import models

# Create your models here.

class Room(models.Model):
    room_number = models.CharField(max_length=75)
    bed_type = models.CharField(max_length=75)
    rate = models.IntegerField()
    smoking = models.BooleanField()
    occupant_name = models.CharField(max_length=75)
    is_occupied = models.BooleanField()

    def __str__(self):
        return self.room_number