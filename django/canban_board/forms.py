
from .models import Card
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


def check_user(value):
    users = User.objects.only("username")
    for each in users:
        if value == str(each):
            raise ValidationError(
                _('%(value)s is already registered. Try others names.'),
                params={'value': value})


class CardForm(forms.ModelForm):

    class Meta:
        model = Card
        fields = ('name', 'description', 'start_date', 'end_date',
                  'state')


class UserForm(forms.Form):
    username = forms.CharField(max_length=150, validators=[check_user])
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    password_again = forms.CharField(label='Password again', widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_again = cleaned_data.get("password_again")

        if password != password_again:
            raise forms.ValidationError(
                "The fields Password and Password again  do not match. Try again.")
