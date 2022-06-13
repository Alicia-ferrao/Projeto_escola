from django import forms
from django.contrib.auth.models import User
from app_users.models import User_profile
from django.contrib.auth.forms import UserCreationForm


class Userform(UserCreationForm):
    email = forms.EmailField()
    fields = ('usename', 'firstname', 'lastname', 'email', 'password1', 'password2')

    labels ={
        'password1' : 'password1',
        'password2' : 'password2',

   }


class UserProfileInfoForm(forms.ModelForm):
    bio = forms.CharField(required=False)
    Professor = 'Professor' 
    Estudante = 'Estudante'  
    USER_TYPES = (
    ('Professor', 'Professor'),
    ('Estudante', 'Estudante'),
   
)
    user_type = forms.ChoiceField(required=True, choices=USER_TYPES)


    class Meta():
        model = User_profile
        fields = ('bio', 'imagem', 'user_type')