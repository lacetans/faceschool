from models import FSUser, Post
from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = FSUser
        fields = ('profile_image',)

class newAdForm(forms.ModelForm):
    class Meta:
        model = Post
