from django import forms

from .models import Eleves

class StudentForm(forms.Form):
   
    GENDER_CHOICES = (
        ('h','Homme'),
        ('f','Femme'),
    )
    CLASSE_CHOICES = (
        ('terminale','terminale'),
        ('premier','premier'),
        ('second','second'),
        ('troisieme','troisieme'),
        ('quatrieme','quatrieme'),
        ('cinquieme','cinquieme'),
    )
    Nom = forms.CharField(max_length=15)
    Prenoms = forms.CharField(max_length=255)
    Genre = forms.ChoiceField( choices=GENDER_CHOICES,widget= forms.RadioSelect)
    Matricule= forms.CharField(max_length=15)
    Date_Naissance = forms.DateField(widget=forms.DateInput)
    Classe= forms.ChoiceField(choices=CLASSE_CHOICES)
    Telephone=forms.CharField(max_length=30)
    Ville=forms.CharField(max_length=30)

class MyFormStudent(forms.ModelForm):
    class Meta:
        model = Eleves
        fields = ['nom','prenom', 'ville', 'telephone', 'classe','age','genre', 'matricule'  ]  # Spécifie les champs à inclure dans le formulaire     