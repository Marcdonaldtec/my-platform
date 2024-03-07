from django import forms
from .models import UserProfile
from django.contrib.auth.forms import UserChangeForm

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'email', 'phone', 'photo']

class UpdatePersonalInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'gender', 'phone','photo', 'email']

class UpdateAccountInfoForm(UserChangeForm):  
    class Meta:
        model = UserProfile  
        fields = ['email']  

