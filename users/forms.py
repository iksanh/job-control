from django import forms

class LoginForm(forms.Form):
    user = forms.CharField(max_length=60)
    password = forms.CharField(max_length=60, widget=forms.PasswordInput)
