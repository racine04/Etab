from django.db import models
from base.models.person import Person




# Create your models here.
MATTER = [
    ('Math', 'Math'),
    ('SVT', 'SVT'),
    ('Anglais', 'Anglais'),
    ('Physique', 'Physique'),
    ('EPS', 'EPS'),
    ('Philosophie', 'Philosophie'),
    ('Francais', 'Francais'),
]

VACANT = [
    ('Oui', 'Oui'),
    ('Non', 'Non'),
]

GENDER = [
    ('F', 'Female'),
    ('M', 'Male'),
    ('O', 'Other'),
]

class TeacherModel(Person):
    vacant = models.CharField(max_length=50, choices= VACANT)
    matiere_enseigne = models.CharField(max_length=30, choices= MATTER)
    

    def __str__(self):
        return self.nom
    
    


        