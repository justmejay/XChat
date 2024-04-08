from django import forms
from .models import Messages


class SentMessage(forms.ModelForm):
    class Meta:
        model = Messages
        fields = ['nickname','message']
