from django import forms

from .models import Utilisateurs

class UsersForm(forms.Form):
   
    
    pseudo = forms.CharField(max_length=10)
    mot_de_passe = forms.CharField(max_length=128)
    confirmer_mot_de_passe= forms.CharField(max_length=255)

class MyForm(forms.ModelForm):
    class Meta:
        model = Utilisateurs
        fields = ['pseudo', 'mot_de_passe']  # Spécifie les champs à inclure dans le formulaire 
        widgets = {
            'mot_de_passe': forms.PasswordInput(),  # Utilisez PasswordInput pour les champs de mot de passe
        } 