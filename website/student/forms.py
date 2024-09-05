from django import forms

from student.models.absence import AbsenceModel
from student.models.card import StudentCardModel

from .models.student import StudentModel




class MyFormStudent(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = ['nom','prenom', 'telephone','age','genre', 'picture', 'matricule', 'adress', 'classe', 'user'  ]  # Spécifie les champs à inclure dans le formulaire 

class AbsenceForm(forms.ModelForm):
    class Meta:
        model = AbsenceModel
        fields = ['absence_date', 'absence_number', 'eleves'  ]

class StudentCardForm(forms.ModelForm):
    class Meta:
        model = StudentCardModel
        fields = "__all__"     
                      