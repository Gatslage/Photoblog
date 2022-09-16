
from dataclasses import fields
from django import forms
from blog import models

class PhotoForm(forms.ModelForm):
    class Meta:
        model=models.Photo
        fields=('image','caption')

class blogForm(forms.ModelForm):
    upd_blog=forms.BooleanField(widget=forms.HiddenInput,initial=True)
    class Meta:
        model=models.Blog
        fields=('title','content')
class deleteForm(forms.Form):
    del_blog=forms.BooleanField(widget=forms.HiddenInput,initial=True)
    
