from django import forms
from .models import People

class LoginForm(forms.Form):
    user = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())

    def clean_user(self):
        username = self.cleaned_data.get('login_email')
        user = People.objects.filter(name = username)

        if not user:
            raise forms.ValidationError('This user does not exist')


