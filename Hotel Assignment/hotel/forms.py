from django import forms
from . import models
class createHotel(forms.ModelForm):
    class Meta:
        model = models.Hotel
        fields = ['name', 'address', 'number_of_rooms', 'occupied_rooms']