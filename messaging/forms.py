from django import forms


class ThreadForm(forms.Form):
    username = forms.CharField(label='', max_length=100)

