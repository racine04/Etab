from django import forms

from .models import Professeurs

class ProfessorForm(forms.Form):
   
    GENDER_CHOICES = (
        ('h','Homme'),
        ('f','Femme'),
    )
    MATTER_CHOICES = (
        ('Math','Math'),
        ('Physique','Physique'),
        ('EPS','EPS'),
        ('Anglais','Anglais'),
        ('SVT','SVT'),
        ('Philosophie','Philosophie'),
        ('Français','Français'),
    )
    Nom = forms.CharField(max_length=15)
    Prenoms = forms.CharField(max_length=255)
    Genre = forms.ChoiceField( choices=GENDER_CHOICES,widget= forms.RadioSelect)
    Date_Naissance = forms.DateField(widget=forms.DateInput)
    Matiere= forms.ChoiceField(choices=MATTER_CHOICES)
    Telephone=forms.CharField(max_length=30)
    Ville=forms.CharField(max_length=30)


class MyFormProf(forms.ModelForm):
    class Meta:
        model = Professeurs
        fields = ['nom','prenom', 'ville', 'telephone', 'vacant', 'age', 'matiere_enseigne', 'prochain_cours', 'sujet_prochaincours'   ]  # Spécifie les champs à inclure dans le formulaire 
        
 