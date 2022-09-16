from django import forms
from authentication.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class loginForm(forms.Form):
        username=forms.CharField( min_length=3,max_length=70, required=True)
        password=forms.CharField(min_length=3,max_length=70,widget=forms.PasswordInput,required=True)
        
class registerForm(UserCreationForm):
        class Meta(UserCreationForm.Meta):
                model = get_user_model()
                fields= ('username', 'email', 'first_name', 'last_name', 'role')
class profilForm(forms.ModelForm):
        class Meta:
                model=User
                fields=('profil',)
class followForm(forms.ModelForm):
        
        class Meta:
                model=User
                fields=['follows']
