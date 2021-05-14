
from .models import Card
from django import forms


class CardForm(forms.ModelForm):

    class Meta:
        model = Card
        fields = ('name', 'description', 'start_date', 'end_date',
                  'state')
