from django import forms


class GuestForm(forms.Form):
    username = forms.CharField()
    text = forms.CharField()


