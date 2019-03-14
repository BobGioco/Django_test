from django import forms
from django.contrib.auth.models import User
from Project_app.models import UserProfileInfo

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())#just if we want to edit it
    class Meta():
        model=User
        fields=('username','email','password','last_name')#set up fields you want to know from users

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model=UserProfileInfo
        fields=('portfolio_site','profile_pic')
