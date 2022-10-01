from django import forms
from django.forms import widgets

class GuestForm(forms.Form):
    author = forms.CharField(max_length=100, required=True, label='Имя ',
                                widget=forms.TextInput({'class': 'form-input'}))
    email = forms.EmailField(max_length=200, required=True, label='Email ')
    description = forms.CharField(max_length=2000, required=True, label='Текст',
                                    widget=widgets.Textarea)
