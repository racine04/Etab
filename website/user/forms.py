from django import forms

from .models.role_user import  RoleUserModel
from .models.user import UserModel


class UsersForm(forms.Form):   
    pseudo = forms.CharField(max_length=10)
    mot_de_passe = forms.CharField(max_length=128)
    confirmer_mot_de_passe= forms.CharField(max_length=255)

class MyUserForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['pseudo', 'mot_de_passe', 'role', 'school']  # Spécifie les champs à inclure dans le formulaire 
        widgets = {
            'mot_de_passe': forms.PasswordInput(),  # Utilisez PasswordInput pour les champs de mot de passe
        } 

class RoleUserForm(forms.ModelForm):
    class Meta:
        model = RoleUserModel
        fields = ['role_user']  # Spécifie les champs à inclure dans le formulaire 



  # Spécifie les champs à inclure dans le formulaire                 
                