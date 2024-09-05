from django.db import models

from base.models.person import Person



GENDER = [
    ('F', 'Female'),
    ('M', 'Male'),
    ('O', 'Other'),
]

CLASSE_CHOICES = (
        ('terminale','terminale'),
        ('premiere','premiere'),
        ('seconde','seconde'),
        ('troisieme','troisieme'),
        ('quatrieme','quatrieme'),
        ('cinquieme','cinquieme'),
    )


class StudentModel(Person):
    
    matricule = models.CharField(max_length=50)
    classe = models.CharField(max_length=50, choices=CLASSE_CHOICES)
    parent_number = models.CharField(max_length=50)
    
    

    def __str__(self):
     return f"{self.nom} {self.prenom}"

