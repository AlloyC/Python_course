from django import forms

class SignupForm(forms.Form):
    firstname = forms.CharField(max_length=100)
    lastname = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    birthday = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))