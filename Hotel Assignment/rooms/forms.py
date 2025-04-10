from django import forms
from . import models

class CreateRoom(forms.ModelForm):
    class Meta:
        model = models.Room
        fields = ['room_number','bed_type','rate','smoking','occupant_name','is_occupied']
