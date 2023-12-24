# forms.py
from django import forms
from .models import Participant

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = '__all__'  # Include all fields from your model
