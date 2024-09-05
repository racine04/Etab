from django import forms

from .models.teacher import TeacherModel

class TeacherForm(forms.ModelForm):
    class Meta:
        model = TeacherModel
        fields = ['nom','prenom', 'telephone', 'vacant', 'age', 'matiere_enseigne', 'genre', 'adress', 'user'  ]  # Spécifie les champs à inclure dans le formulaire 
         
        
     
 