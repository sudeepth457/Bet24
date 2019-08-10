from django import forms
from django.contrib.auth.models import User
from .models import Userprofile
class UserForm(forms.Form):
    username = forms.CharField(label="")
    password = forms.CharField(label="",widget=forms.PasswordInput)
class UserRegistration(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter password here.....'}))
    confirm_password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Confirm password here.....'}))
    class Meta:
        model=User
        fields=(
        'username',
        'first_name',
        'last_name',
        'email',
        )
    def clean_confirm_password(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError('password mismatch')
        return confirm_password

class userprofileform(forms.ModelForm):
    class Meta:
        model = Userprofile
        fields = ('phone','country')
