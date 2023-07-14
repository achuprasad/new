from django import forms
from .models import Ticket

class TicketForm(forms.ModelForm):
    social_media_platform = forms.ChoiceField(choices=[('facebook', 'Facebook'), ('pinterest', 'Pinterest')])

    class Meta:
        model = Ticket
        fields = ['name', 'email', 'phone', 'country', 'social_media_platform']
