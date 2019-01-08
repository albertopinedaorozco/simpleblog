from django import forms

from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username','email','age',)#UserCreationForm.Meta.fields + ('age','picture',)

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = fields = ('username','email','age',) #UserChangeForm.Meta.fields 
