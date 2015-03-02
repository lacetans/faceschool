# -*- encoding: utf-8 -*-

from models import FSUser, Post
from django.contrib.auth.models import User
from django import forms
from django.core import validators
from models import Badws, Goodws, Removebadws, Removegoodws, Badwsmasiva, Goodwsmaisva

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = FSUser
        fields = ('profile_image',)

class newPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text', 'image','channel','user')
        labels = {
			'text':'text',
			'image':'image',
        }
        widgets = {
            'text': forms.Textarea(attrs={'cols': 80, 'rows': 5, 'placeholder': 'En què penses?'}),
        }



class PostForm(forms.ModelForm):
 
   class Meta:
      model = Post

class BadwForm(forms.ModelForm):
 
   class Meta:
      model = Badws

class GoodwForm(forms.ModelForm):
 
   class Meta:
      model = Goodws

class RemovebadwForm(forms.ModelForm):
 
   class Meta:
      model = Badws

class RemovegoodwForm(forms.ModelForm):
 
   class Meta:
      model = Goodws

class BadwmasivaForm(forms.ModelForm):
 
   class Meta:
      model = Badwsmasiva

class GoodwmasivaForm(forms.ModelForm):
 
   class Meta:
      model = Goodwsmasiva
