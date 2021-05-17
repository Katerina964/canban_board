
from .models import Card
from django import forms


class CardForm(forms.ModelForm):

    class Meta:
        model = Card
        fields = ('name', 'description', 'start_date', 'end_date',
                  'state')

        widgets = {
            'start_date': forms.DateInput(format=('%Y-%m-%d'),
                                          attrs={'placeholder': "Введите пароль для авторизации на сайте"}),
            'end_date': forms.DateInput(format=('%Y-%m-%d'))}
