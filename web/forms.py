from django import forms
from models import Post
from models import Badws
from models import Goodws
from models import Removebadws
from models import Removegoodws
from models import Badwsmasiva
from models import Goodwsmasiva

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

